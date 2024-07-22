#-----------------------------------------------------------
# Copyright (C) 2015 Martin Dobias
#-----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#---------------------------------------------------------------------
import decimal
import os.path

from PyQt5.QtWidgets import QAction, QMessageBox, QMenu, QComboBox, QWidgetAction, QProgressBar
from qgis._core import QgsMessageLog, QgsProcessingFeedback

from .sincronizacion.bbdd_eiel import BBDDEiel
from .sincronizacion.sincronizador import Sincronizador
from .util import revisar_estado, identificar_host_conexion_actual, obtener_conexion_local, obtener_conexion_remoto
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsDataSourceUri, QgsProject, QgsMapLayer, QgsSettings, Qgis
from .ui.dlg_config import ConfigDialog
from qgis.utils import iface
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from osgeo import gdal
import locale
import configparser


def classFactory(iface):
    return SerEIELPlugin(iface)


class SerEIELPlugin:

    def __init__(self, iface):
        self.iface = iface
        self.conexion = ""


    def initGui(self):
        self.conexion = ""
        self.menu = QMenu(self.iface.mainWindow())
        self.menu.setObjectName("menuSerEIEL")
        self.menu.setTitle("SerEIEL")

        self.toolbar = self.iface.addToolBar('SerEIEL')
        self.toolbar.setObjectName("menuSerEIEL")
        self.toolbar.setToolTip('menuSerEIEL')
        locale.setlocale(locale.LC_ALL, 'es_ES')

        self.actionConfig = QAction(QIcon(":/SerEIEL/resources/icon/gear-solid.svg"), "Configuración", self.iface.mainWindow())
        self.actionConfig.setObjectName("actionConfig")
        self.actionConfig.setToolTip('Configuración')
        self.actionConfig.triggered.connect(self.mostrar_config)
        self.menu.addAction(self.actionConfig)
        self.toolbar.addAction(self.actionConfig)
        self.con = psycopg2.connect(
            "host='eielzamora' port='5432' dbname='eiel_zamora' user='postgres' password='admin@985' connect_timeout=10 ")

        #self.cb = QComboBox(self.iface.mainWindow())
        #self.cb.addItem("0001")
        #self.cb.addItem("0002")
        #self.cbAction = self.toolbar.addWidget(self.cb)

        self.actionCambiarConexion = QAction(QIcon(":/SerEIEL/resources/icon/cloud-arrow-up-solid.svg"),"Cambiar conexión", self.iface.mainWindow())
        self.actionCambiarConexion.setObjectName("actionCambiarConexion")
        self.actionCambiarConexion.setWhatsThis("Cambia la conexión de servidor a local")
        self.actionCambiarConexion.triggered.connect(self.cambiar_conexion)
        self.menu.addAction(self.actionCambiarConexion)
        self.toolbar.addAction(self.actionCambiarConexion)


        self.actionSincronizar = QAction(QIcon(":/SerEIEL/resources/icon/cloud-arrow-up-solid.svg"), "Sincronizar", self.iface.mainWindow())
        self.actionSincronizar.setObjectName("actionSincronizar")
        self.actionSincronizar.setWhatsThis("Sincronizar BBDD local con servidor")
        self.actionSincronizar.triggered.connect(self.sincronizar)
        self.menu.addAction(self.actionSincronizar)
        self.toolbar.addAction(self.actionSincronizar)

        self.actionExportar = QAction(QIcon(":/SerEIEL/resources/icon/cloud-arrow-up-solid.svg"), "Exportar", self.iface.mainWindow())
        self.actionExportar.setObjectName("actionExportar")
        self.actionExportar.setWhatsThis("Exporta al formato de entrega en shape y txt")
        self.actionExportar.triggered.connect(self.exportar)
        self.menu.addAction(self.actionExportar)
        self.toolbar.addAction(self.actionExportar)

        #self.actionExportarEntrega = QAction(QIcon(":/SerEIEL/resources/icon/file-export-solid.svg"), "Exportar entrega", self.iface.mainWindow())
        #self.actionExportarEntrega.setObjectName("actionExportarEntrega")
        #self.actionExportarEntrega.setWhatsThis("Exportar a formato entrega")
        #self.actionExportarEntrega.triggered.connect(self.run)
        #self.menu.addAction(self.actionExportarEntrega)
        #self.toolbar.addAction(self.actionExportarEntrega)


        self.definir_mensaje_boton_cambiar_conexion()

        self.menuBar = self.iface.mainWindow().menuBar()
        self.menuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.menu)


    def definir_mensaje_boton_cambiar_conexion(self):
        host = identificar_host_conexion_actual()
        self.conexion = ""
        if host == "localhost":
            self.conexion = "local"
            self.actionCambiarConexion.setText("Conectado a local")
        elif host == QgsSettings().value("SerEIEL/pgremoto_host"):
            self.conexion = "remoto"
            self.actionCambiarConexion.setText("Conectado a remoto")

    def unload(self):
        self.iface.removeToolBarIcon(self.actionConfig)
        del self.actionConfig

        self.iface.removeToolBarIcon(self.actionCambiarConexion)
        del self.actionCambiarConexion

        self.iface.removeToolBarIcon(self.actionSincronizar)
        del self.actionSincronizar

        self.menu.deleteLater()

    def sincronizar(self):
        mensajes_error = revisar_estado()
        if len(mensajes_error) > 0:
            iface.messageBar().pushMessage("SerEIEL", mensajes_error, level=Qgis.Warning)
            return

        respuesta = QMessageBox.question(self.iface.mainWindow(),
                             "SerEIEL",
                             "Al sincronizar se van a subir los cambios realizados " +
                             "y descargar las modificaciones existentes en el servidor. ¿Continuar?",
                             QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.No:
            return

        QgsMessageLog.logMessage('** INICIANDO SINCRONIZACION ********', 'SerEIEL', Qgis.Info)
        with BBDDEiel(obtener_conexion_remoto()) as bbdd_remota:
            with BBDDEiel(obtener_conexion_local()) as bbdd_local:
                sincronizador = Sincronizador(bbdd_local, bbdd_remota)
                sincronizador.sincronizar_capas_trabajo()
        
        QgsMessageLog.logMessage('** SINCRONIZACION FINALIZADA!!! *********', 'SerEIEL', Qgis.Info)
        QMessageBox.information(iface.mainWindow(), 'SerEIEL plugin', 'Sincronización finalizada')

    def mostrar_config(self):
        dlg = ConfigDialog(self.iface.mainWindow())
        dlg.exec_()

    def cambiar_conexion_normal(self):
        self.cambiar_conexion(True)

    def cambiar_conexion_remoto(self):
        self.cambiar_conexion(True)

    def cambiar_conexion(self, resetear_conexion_a_remoto):

        conexion_dest = "remoto"
        if self.conexion == "":
            self.definir_mensaje_boton_cambiar_conexion()
            if self.conexion == "":
                respuesta = QMessageBox.question(iface.mainWindow(), "SerEIEL",
                                                 "No se puede identificar el proyecto actual. ¿Conectar a tu configuración de remoto?",
                                                 QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.No:
                    return
                else:
                    resetear_conexion_a_remoto = True

        if not resetear_conexion_a_remoto:
            mensajes_error = revisar_estado()
            if 'La conexión local no es válida' in mensajes_error and not 'La conexión remota no es válida' in mensajes_error:
                respuesta = QMessageBox.question(
                    iface.mainWindow(),
                    "SerEIEL",
                    "No tienes la conexión local funcionando, pero si la remota. ¿Forzar conexión a remoto?",
                    QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    resetear_conexion_a_remoto = True

            if not resetear_conexion_a_remoto:
                if len(mensajes_error) > 0:
                    iface.messageBar().pushMessage("SerEIEL", mensajes_error, level=Qgis.Warning)
                    return

                if self.conexion == "remoto":
                    conexion_dest = "local"

                respuesta = QMessageBox.question(iface.mainWindow(), "SerEIEL", "¿Cambiar la conexión a %s?" % conexion_dest,
                                                 QMessageBox.Yes, QMessageBox.No)
                if respuesta == QMessageBox.No:
                    return

        s = QgsSettings()
        if self.conexion == "local" or resetear_conexion_a_remoto:
            self.conexion = conexion_dest
            self.server = s.value("SerEIEL/pgremoto_host")
            self.port = s.value("SerEIEL/pgremoto_puerto")
            self.bbdd = s.value("SerEIEL/pgremoto_bbdd")
            self.user = s.value("SerEIEL/pgremoto_usuario")
            self.passw = s.value("SerEIEL/pgremoto_password")
        else:
            self.conexion = conexion_dest
            self.server = s.value("SerEIEL/pglocal_host")
            self.port = s.value("SerEIEL/pglocal_puerto")
            self.bbdd = s.value("SerEIEL/pglocal_bbdd")
            self.user = s.value("SerEIEL/pglocal_usuario")
            self.passw = s.value("SerEIEL/pglocal_password")

        for layer in QgsProject.instance().mapLayers().values():

            if layer.type() == QgsMapLayer.VectorLayer:
                provider = layer.dataProvider().name()
                source_uri = layer.dataProvider().uri()

                if provider == "postgres":
                    uri = QgsDataSourceUri()
                    uri.setConnection(self.server, self.port, self.bbdd, self.user, self.passw)
                    uri.setDataSource(source_uri.schema(), source_uri.table(), source_uri.geometryColumn(), source_uri.sql(), source_uri.keyColumn())
                    uri.setSrid(source_uri.srid())
                    print(layer.name() + " - " + uri.uri())
                    layer.setDataSource(uri.uri(), layer.name(), 'postgres')

        #QMessageBox.information(iface.mainWindow(), 'SerEIEL plugin', 'Conectado a ' + self.conexion)
        self.actionCambiarConexion.setText("Conectado a " + self.conexion)
        iface.messageBar().pushMessage("SerEIEL", "Conectado a " + self.conexion, level=Qgis.Success)

    def exportar(self):
        s = QgsSettings()
        directorio_salida = self.server = s.value("SerEIEL/ruta_exportacion")

        #directorio_salida_txt = "C:\EIEL Zamora\Exportacion_txt"
        progressMessageBar = iface.messageBar()
        progressbar = QProgressBar()
        progressbar.setTextVisible(True)
        progressMessageBar.pushWidget(progressbar)
        gdal.UseExceptions()

        directorio_actual = os.path.dirname(os.path.realpath(__file__))


        config = configparser.ConfigParser()
        config.read(directorio_actual + '/exportacion.ini')

        self.valor = 0
        self.total = len(config['shape']) + len(config['txt']) + len(config['postgresql'])

        for nombre in config['shape']:
            self.exportar_shape(progressbar, directorio_salida, nombre, config['shape'][nombre])

        for nombre in config['txt']:
            self.exportar_txt(self.con, progressbar, directorio_salida, self.mayusculas(str(nombre)), config['txt'][nombre])

        for nombre in config['postgresql']:
            self.exportar_postgresql(progressbar, nombre, config['postgresql'][nombre])

        progressbar.setFormat('Finalizado')
        progressbar.setValue(100)

    def exportar_shape(self, progressbar, directorio_salida, nombre, sql):
        try:
            self.valor += 1
            progressbar.setFormat('Exportando {}...'.format(nombre))
            progressbar.setValue(int(self.valor * 100 / self.total))
            ds = gdal.VectorTranslate(
                destNameOrDestDS=directorio_salida + "/" + nombre + ".shp",
                srcDS="PG:dbname=eiel_zamora host=eielzamora port=5432 user=postgres password=admin@985",
                format="ESRI Shapefile",
                SQLStatement=sql
            )
        except Exception as e:
            #print(f"Error generando shape en la capa: {e}" + nombre)
            QgsMessageLog.logMessage(f"Error generando shape en la capa: {e}", 'SerEIEL', Qgis.Warning)

    def tostring(self, valor):
        if isinstance(valor, (decimal.Decimal or '99', float)):
            return str(valor).replace('.', ',')
        else:
            valorstr = str(valor or '')
            if valor == 0:
                valorstr = '0'
            return valorstr

    def mayusculas(self, nombre):
        return nombre.upper()

    def exportar_txt(self, con, progressbar, directorio_salida, nombre, sql):
        try:
            cur = con.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            self.valor += 1
            progressbar.setFormat('Exportando {}...'.format(nombre))
            progressbar.setValue(int(self.valor * 100 / self.total))
            with open(directorio_salida + "/" + nombre + ".txt", "w") as f:
                for row in rows:
                    f.write("|".join(list(map(self.tostring, row))))
                    f.write('\n')

        except Exception as e:
            QgsMessageLog.logMessage(f"Translation failed: {e}", 'SerEIEL', Qgis.Warning)

    def exportar_postgresql(self, progressbar, nombre, sql):
        try:
            self.valor += 1
            progressbar.setFormat('Exportando {}...'.format(nombre))
            progressbar.setValue(int(self.valor * 100 / self.total))
            conn_string = "PG:dbname=mapstorm-eiel host=eielzamora port=5432 user=postgres password=admin@985"
            gdal.UseExceptions()
            ds = gdal.OpenEx(conn_string, gdal.OF_VECTOR)

            gdal.VectorTranslate(
                ds,
                srcDS="PG:dbname=eiel_zamora host=eielzamora port=5432 user=postgres password=admin@985",
                SQLStatement=sql,
                accessMode='overwrite',
                layerName='eiel.' + nombre
            )
        except Exception as e:
            QgsMessageLog.logMessage(f"Error en postgis al generar la capa: " + nombre + f"{ gdal.GetLastErrorMsg() }", 'SerEIEL', Qgis.Warning)
            #QgsMessageLog.logMessage(f"Error generando postgis en la capa: {gdal.GetLastErrorMsg()}", 'SerEIEL', Qgis.Warning)

            # ds = gdal.VectorTranslate(
            #     destNameOrDestDS="PG:dbname=mapstorm-eiel host=eielzamora port=5432 user=postgres password=admin@985",
            #     srcDS="PG:dbname=mapstorm-eiel host=eielzamora port=5432 user=postgres password=admin@985",
            #     format="PostgreSQL",
            #     SQLStatement=sql
            # )





