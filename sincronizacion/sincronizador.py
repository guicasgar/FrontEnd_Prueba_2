import os
from datetime import date
from qgis.core import QgsMessageLog, Qgis
from .bbdd_eiel import BBDDEiel
from .estado import Estado
from itertools import groupby
from PyQt5.QtWidgets import QMessageBox


def identificar_altas(eregistros, uuids):
    for uuid in eregistros.keys():
        if eregistros[uuid].estado == Estado.Modificado:
            if uuid not in uuids:
                eregistros[uuid].estado = Estado.Alta


def identificar_modificados(eregistros, eregistros_comp):
    for uuid in eregistros.keys():
        if eregistros[uuid].estado == Estado.Modificado:
            if uuid in eregistros_comp:
                if eregistros_comp[uuid].estado != Estado.Baja:
                    eregistros[uuid].comparar(eregistros_comp[uuid])
                else:
                    eregistros[uuid].estado = Estado.ConflictoModificadoBaja


def identificar_cambios(eregistros_local, eregistros_remoto, uuids_local, uuids_remoto):
    identificar_altas(eregistros_local, uuids_remoto)
    identificar_altas(eregistros_remoto, uuids_local)
    identificar_modificados(eregistros_local, eregistros_remoto)
    identificar_modificados(eregistros_remoto, eregistros_local)


def imprimir(eregistros, capa, texto):
    if len(eregistros) == 0:
        return
    QgsMessageLog.logMessage('CAPA %s CAMBIOS EN %s' % (capa, texto.upper()), 'SerEIEL', Qgis.Info)
    ereg_por_estado = groupby(sorted(eregistros.values(), key=lambda x: str(x.estado)), lambda x: x.estado)
    for estado, ereg in ereg_por_estado:
        imprimir_tipo(list(ereg), str(estado))


def imprimir_tipo(eregistros, tipo):
    if len(eregistros) > 0:
        QgsMessageLog.logMessage('....' + tipo, 'SerEIEL', Qgis.Info)
    for reg in eregistros:
        QgsMessageLog.logMessage('........' + repr(reg), 'SerEIEL', Qgis.Info)
        if reg.estado == Estado.Modificado:
            for dif in reg.diferencias:
                QgsMessageLog.logMessage('............[%s] - (%s) -> (%s)' % dif, 'SerEIEL', Qgis.Info)


class Sincronizador:
    
    def __init__(self, bbdd_local: BBDDEiel, bbdd_remota: BBDDEiel):
        self._bbdd_local = bbdd_local
        self._bbdd_remota = bbdd_remota
        self._usuario = os.getlogin()
        self._fecha = date.today()
        self._fecha_ultimo_backup = None
    
    def sincronizar_capas_trabajo(self):
        self._fecha_ultimo_backup = self._bbdd_remota.obtener_fecha_ultimo_backup(self._usuario)
        self._bbdd_remota.registrar_sincronizacion()
        self._bbdd_local.registrar_sincronizacion()
        capas = self._bbdd_remota.obtener_capas_trabajo()
        for capa in capas:
            try:
                self.sincronizar_capa(capa)
            except Exception as e:
                self._bbdd_remota.registrar_sincronizacion_capa_error(capa, 'ERROR ' + str(e))
                self._bbdd_local.registrar_sincronizacion_capa_error(capa, 'ERROR ' + str(e))
        
    def sincronizar_capa(self, capa):
        fecha_ult_sincro_remota = self._bbdd_remota.obtener_fecha_ultima_sincronizacion_capa(self._usuario, capa)
        if fecha_ult_sincro_remota is None:
            fecha_ult_sincro_remota = self._fecha_ultimo_backup
        fecha_ult_sincro_local = self._bbdd_local.obtener_fecha_ultima_sincronizacion_capa(self._usuario, capa)
        if fecha_ult_sincro_local is None:
            fecha_ult_sincro_local = self._fecha_ultimo_backup
        fecha_ult_sincro = max(fecha_ult_sincro_local, fecha_ult_sincro_remota)
        fecha_ult_sincro = max(fecha_ult_sincro, self._fecha_ultimo_backup)
        QgsMessageLog.logMessage('Capa %s sincronizada ultima vez %s' % (capa, str(fecha_ult_sincro)), 'SerEIEL', Qgis.Info)
        eregistros_remoto = self._bbdd_remota.obtener_estados_registros_desde(capa, fecha_ult_sincro)
        uuids_remoto = self._bbdd_remota.obtener_uuids(capa)
        eregistros_local = self._bbdd_local.obtener_estados_registros_desde(capa, fecha_ult_sincro)
        uuids_local = self._bbdd_local.obtener_uuids(capa)
        identificar_cambios(eregistros_local, eregistros_remoto, uuids_local, uuids_remoto)
        imprimir(eregistros_local, capa, 'local')
        imprimir(eregistros_remoto, capa, 'servidor')
        self._bbdd_remota.guardar(capa, eregistros_local)
        self._bbdd_local.guardar(capa, eregistros_remoto)
        self._bbdd_local.registrar_envios(self._bbdd_remota.sincronizaciones)
        self._bbdd_remota.registrar_envios(self._bbdd_local.sincronizaciones)

        
        
