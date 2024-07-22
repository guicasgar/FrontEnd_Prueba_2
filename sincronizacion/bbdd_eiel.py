from .estado import Estado
from .estado_registro import EstadoRegistro
from psycopg2._psycopg import connection
from psycopg2.extras import RealDictCursor
from qgis._core import Qgis, QgsMessageLog
import os
from datetime import datetime

from ..util import obtener_version_plugin


class BBDDEiel:
    
    def __init__(self, conn: connection):
        self._conn = conn
        self._id_sincro = -1
        self.sincronizaciones = []
        os.environ['PGTZ'] = 'Europe/Madrid'
        
    def obtener_fecha_ultima_sincronizacion(self, usuario):
        cur = self._conn.cursor()
        cur.execute("""select max(fecha) from informes.sincronizaciones where usuario = '%s'""" % usuario)
        rows = cur.fetchall()
        if len(rows) == 0:
            raise Exception("No se encontró el usuario %s en la tabla 'sincronizaciones' del esquema 'informes'")
        cur.close()
        return rows[0][0]
    
    def obtener_fecha_ultimo_backup(self, usuario):
        cur = self._conn.cursor()
        cur.execute("""select max(fecha) from informes.sincronizaciones where usuario = '%s' and equipo = 'BACKUP';""" % usuario)
        rows = cur.fetchall()
        if len(rows) == 0:
            raise Exception("No se encontró registro backup para el usuario %s en la tabla 'sincronizaciones' del esquema 'informes'")
        cur.close()
        return rows[0][0]
    
    def obtener_fecha_ultima_sincronizacion_capa(self, usuario, capa):
        cur = self._conn.cursor()
        sql = """select max(fecha)
                    from informes.sincronizaciones s
                        left join informes.resultados_sincronizacion r on s.id = r.id_sincronizacion
                    where usuario = %s and tabla = %s and comentario = 'Sincronizacion OK'"""
        cur.execute(sql, (usuario, capa))
        rows = cur.fetchall()
        fecha = None
        if len(rows) > 0:
            fecha = rows[0][0]
        cur.close()
        return fecha
    
    def obtener_capas_trabajo(self):
        cur = self._conn.cursor()
        cur.execute(
            """select table_name
                    from information_schema."tables" t
                    where table_schema = 'eiel' and table_name not like 'qgis_%'
                    and exists (select 1 from information_schema.columns c where c.table_schema = 'eiel' and c.table_name = t.table_name and c.column_name = 'ser_uuid')
                    order by table_name;""")
        capas = []
        for row in cur.fetchall():
            capas.append(row[0])
        return capas
    
    def obtener_uuids(self, capa):
        uuids = self.obtener_uuids_activos(capa)
        uuids_baja = self.obtener_uuids_borrados(capa)
        return uuids + uuids_baja
    
    def obtener_uuids_activos(self, capa):
        cur = self._conn.cursor()
        cur.execute("""select ser_uuid from eiel.\"%s\" """ % capa)
        uuids = []
        for row in cur.fetchall():
            uuids.append(row[0])
        cur.close()
        return uuids
    
    def obtener_uuids_borrados(self, capa):
        cur = self._conn.cursor()
        cur.execute("""select ser_uuid from eiel_borrados.\"%s\" """% capa)
        uuids = []
        for row in cur.fetchall():
            uuids.append(row[0])
        cur.close()
        return uuids

    def obtener_estados_registros_desde(self, capa, fecha):
        eregistros_base = self.obtener_estados_registros_capa_principal_desde(capa, fecha)
        eregistros_borrardos = self.obtener_estados_registros_borrados_desde(capa, fecha)
        eregistros = eregistros_base + eregistros_borrardos
        return {ereg.uuid: ereg for ereg in eregistros}

    def obtener_estados_registros_capa_principal_desde(self, capa, fecha):
        cur = self._conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""select * from eiel.\"%s\" where ser_fecha_mod > '%s' """ % (capa, fecha))
        eregistros = []
        for row in cur.fetchall():
            eregistros.append(EstadoRegistro(row))
        
        cur.close()
        return eregistros

    def obtener_estados_registros_borrados_desde(self, capa, fecha):
        cur = self._conn.cursor(cursor_factory=RealDictCursor)
        sql = "select * from eiel_borrados.\"%s\" where ser_fecha_mod  > '%s' " % (capa, fecha)
        cur.execute(sql)
        eregistros_borrar = []
        for row in cur.fetchall():
            ereg = EstadoRegistro(row)
            ereg.estado = Estado.Baja
            eregistros_borrar.append(ereg)
        
        cur.close()
        return eregistros_borrar
    
    def guardar(self, capa, eregistros):
        self.sincronizaciones = []
        altas = [eregistros[r] for r in eregistros if eregistros[r].estado == Estado.Alta]
        bajas = [eregistros[r] for r in eregistros if eregistros[r].estado == Estado.Baja]
        modificaciones = [eregistros[r] for r in eregistros if eregistros[r].estado == Estado.Modificado]
        conflictos = [eregistros[r] for r in eregistros if eregistros[r].estado == Estado.ConflictoModificados]
        conflictos += [eregistros[r] for r in eregistros if eregistros[r].estado == Estado.ConflictoModificadoBaja]
        self.guardar_bajas(capa, bajas)
        self.guardar_modificaciones(capa, modificaciones)
        self.guardar_altas(capa, altas)
        self.guardar_conflictos(capa, conflictos)
        if (len(altas)+len(bajas)+len(modificaciones)+len(conflictos)) > 0:
            self.registrar_sincronizacion_capa(capa, len(altas), len(bajas), len(modificaciones), len(conflictos), 'Recibido')
            
    def guardar_altas(self, capa, eregs):
        if len(eregs) == 0:
            return
        cur = self._conn.cursor()
        cur.execute('SET session_replication_role = replica;')
        self.guardar_inserts(cur, 'eiel', capa, eregs)
        cur.execute('SET session_replication_role = DEFAULT;')
        self._conn.commit()
        
    def guardar_bajas(self, capa, eregs):
        if len(eregs) == 0:
            return
        cur = self._conn.cursor()
        cur.execute('SET session_replication_role = replica;')
        self.guardar_inserts(cur, 'eiel_borrados', capa, eregs)
        self.eliminar_registros(cur, 'eiel', capa, eregs)
        cur.execute('SET session_replication_role = DEFAULT;')
        self._conn.commit()
        
    def guardar_modificaciones(self, capa, eregs):
        if len(eregs) == 0:
            return
        QgsMessageLog.logMessage('MODIFICANDO %s REGISTROS (%s:%s) %s.%s ' % (len(eregs), self._conn.info.host, self._conn.info.port, 'eiel', capa), 'SerEIEL', Qgis.Info)
        campos_ignorar = ['idx']
        cur = self._conn.cursor()
        cur.execute('SET session_replication_role = replica;')
        for ereg in eregs:
            campos = list(ereg.registro.keys())
            campos = [c for c in campos if c not in campos_ignorar]
            campos_format = ['\"%s\" = %s' % (c, '%s') for c in campos]
            valores = [ereg.registro[c] for c in campos]
            sql = 'update \"%s\".\"%s\" set %s where ser_uuid = \'%s\'' % ('eiel', capa, ','.join(campos_format), ereg.uuid)
            #QgsMessageLog.logMessage(str(cur.mogrify(sql, valores)), 'SerEIEL', Qgis.Info)
            cur.execute(sql, valores)
        cur.execute('SET session_replication_role = DEFAULT;')
        self._conn.commit()
    
    def guardar_conflictos(self, capa, eregs):
        if len(eregs) == 0:
            return
        cur = self._conn.cursor()
        cur.execute('SET session_replication_role = replica;')
        for ereg in eregs:
            ereg.registro['ser_confl_descripcion'] = str(ereg.estado)
        self.guardar_inserts(cur, 'eiel_conflictos', capa, eregs)
        cur.execute('SET session_replication_role = DEFAULT;')
        self._conn.commit()
        
    def registrar_envios(self, sincronizaciones_env):
        for sincro in sincronizaciones_env:
            params = list(sincro)
            params[-1] = 'Enviado'
            self.registrar_sincronizacion_capa(params[0], params[1], params[2], params[3], params[4], params[5])
    
    def eliminar_registros(self, cur, esquema, capa, eregs):
        uuids = [r.uuid for r in eregs]
        QgsMessageLog.logMessage('BORRANDO %s REGISTROS (%s:%s) %s.%s ' % (len(eregs), self._conn.info.host, self._conn.info.port, esquema, capa), 'SerEIEL', Qgis.Info)
        sql = 'delete from \"%s\".\"%s\" where ser_uuid::text = any(%s)' % (esquema, capa, '%s')
        #QgsMessageLog.logMessage(str(cur.mogrify(sql, (uuids, ))), 'SerEIEL', Qgis.Info)
        cur.execute(sql, (uuids, ))
        
    def guardar_inserts(self, cur, esquema, capa, eregs):
        campos_ignorar = ['idx']
        if esquema != 'eiel':
            campos_ignorar = ['id']
        QgsMessageLog.logMessage('GUARDANDO %s REGISTROS (%s:%s) %s.%s ' % (len(eregs), self._conn.info.host, self._conn.info.port, esquema, capa), 'SerEIEL', Qgis.Info)
        for ereg in eregs:
            campos = list(ereg.registro.keys())
            campos = [c for c in campos if c not in campos_ignorar]
            campos_format = ['\"' + c + '\"' for c in campos]
            posiciones_valores = ['%s' for c in campos]
            valores = [ereg.registro[c] for c in campos]
            sql = 'insert into \"%s\".\"%s\" (%s) values (%s)' % (esquema, capa, ','.join(campos_format), ','.join(posiciones_valores))
            #QgsMessageLog.logMessage(str(cur.mogrify(sql, valores)), 'SerEIEL', Qgis.Info)
            cur.execute(sql, valores)
    
    def registrar_sincronizacion_capa(self, capa, altas, bajas, modificaciones, conflictos, sentido):
        cur = self._conn.cursor()
        sql = 'insert into informes.resultados_sincronizacion (id_sincronizacion, comentario, tabla, altas, bajas, ' + \
              'modificaciones, conflictos, sentido) values (%s, %s, %s, %s, %s, %s, %s, %s)'
        QgsMessageLog.logMessage(str(cur.mogrify(sql, (self._id_sincro,'Sincronizacion OK', capa, altas, bajas, modificaciones, conflictos, sentido))), 'SerEIEL', Qgis.Info)
        cur.execute(sql, (self._id_sincro,'Sincronizacion OK', capa, altas, bajas, modificaciones, conflictos, sentido))
        self.sincronizaciones.append((capa, altas, bajas, modificaciones, conflictos, sentido))
        self._conn.commit()
        
    def registrar_sincronizacion_capa_error(self, capa, error):
        self._conn.rollback()
        cur = self._conn.cursor()
        sql = 'insert into informes.resultados_sincronizacion (id_sincronizacion, tabla, comentario) values (%s, %s, %s)'
        cur.execute(sql, (self._id_sincro, capa, error))
        self._conn.commit()
    
    def registrar_sincronizacion(self):
        cur = self._conn.cursor()
        sql = 'insert into informes.sincronizaciones (usuario, equipo, app_version) values (%s, %s, %s) RETURNING id'
        cur.execute(sql, (os.getlogin(), os.environ['COMPUTERNAME'], obtener_version_plugin()))
        self._id_sincro = cur.fetchone()[0]
        QgsMessageLog.logMessage('ID SINCRONIZACION: ' + str(self._id_sincro), 'SerEIEL', Qgis.Info)
        self._conn.commit()
    
    def cerrar(self):
        if self._conn is None:
            if not self._conn.closed:
                self._conn.close()
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cerrar()
