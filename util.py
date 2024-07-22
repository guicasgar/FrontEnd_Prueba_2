import psycopg2
import os
from qgis.utils import iface
from qgis.core import Qgis, QgsSettings, QgsProject, QgsMapLayer


def obtener_version_plugin():
    with open(os.path.join(os.path.dirname(__file__), 'metadata.txt')) as file:
        for line in file:
            if line.startswith('version='):
                return line.split('=')[1].strip()
    return '???'


def identificar_host_conexion_actual():
    for layer in QgsProject.instance().mapLayers().values():
        if layer.type() == QgsMapLayer.VectorLayer:
            provider = layer.dataProvider().name()
            source_uri = layer.dataProvider().uri()
            if provider == "postgres":
                return source_uri.host()


def obtener_conexion(host, puerto, bbdd, usuario, password):
    return psycopg2.connect("host='%s' port='%s' dbname='%s' user='%s' password='%s' connect_timeout=10 " %
                            (host, puerto, bbdd, usuario, password))


def obtener_conexion_local():
    s = QgsSettings()
    return obtener_conexion(s.value("SerEIEL/pglocal_host"), s.value("SerEIEL/pglocal_puerto"),
                           s.value("SerEIEL/pglocal_bbdd"), s.value("SerEIEL/pglocal_usuario"),
                           s.value("SerEIEL/pglocal_password"))


def obtener_conexion_remoto():
    s = QgsSettings()
    return obtener_conexion(s.value("SerEIEL/pgremoto_host"), s.value("SerEIEL/pgremoto_puerto"),
                            s.value("SerEIEL/pgremoto_bbdd"), s.value("SerEIEL/pgremoto_usuario"),
                            s.value("SerEIEL/pgremoto_password"))


def conexion_valida(host, puerto, bbdd, usuario, password):
    try:
        conn = obtener_conexion(host, puerto, bbdd, usuario, password)
        conn.close()
        return True
    except:
        return False


def probar_conexion(host, puerto, bbdd, usuario, password):
    if conexion_valida(host, puerto, bbdd, usuario, password):
        msg = "Conectado correctamente a %s en %s(%s) con el usuario %s" % (bbdd, host, puerto, usuario)
        tipo_notificacion = Qgis.Success
    else:
        msg = "No se pudo conectar a %s en %s(%s) con el usuario %s" % (bbdd, host, puerto, usuario)
        tipo_notificacion = Qgis.Critical
    iface.messageBar().pushMessage("SerEIEL", msg, level=tipo_notificacion)


def conexion_remota_valida():
    s = QgsSettings()
    return conexion_valida(s.value("SerEIEL/pgremoto_host"), s.value("SerEIEL/pgremoto_puerto"),
                           s.value("SerEIEL/pgremoto_bbdd"), s.value("SerEIEL/pgremoto_usuario"),
                           s.value("SerEIEL/pgremoto_password"))


def conexione_local_valida():
    s = QgsSettings()
    return conexion_valida(s.value("SerEIEL/pglocal_host"), s.value("SerEIEL/pglocal_puerto"),
                           s.value("SerEIEL/pglocal_bbdd"), s.value("SerEIEL/pglocal_usuario"),
                           s.value("SerEIEL/pglocal_password"))


def hay_capas_en_edicion():
    for layer in QgsProject.instance().mapLayers().values():
        if layer.type() == QgsMapLayer.VectorLayer:
            if layer.isEditable():
                return True
    return False


def revisar_estado():
    problemas = ""
    if not conexion_remota_valida():
        problemas += "La conexión remota no es válida.\n"

    if not conexione_local_valida():
        problemas += "La conexión local no es válida.\n"

    if hay_capas_en_edicion():
        problemas += "Se debe terminar la edición antes de continuar.\n"

    return problemas


