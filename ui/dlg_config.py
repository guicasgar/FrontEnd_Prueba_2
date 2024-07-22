from PyQt5.QtWidgets import  QMessageBox
from qgis.PyQt import uic
from qgis.core import QgsSettings, Qgis
from qgis.PyQt.QtWidgets import QDialog
from qgis.utils import iface
import os
from ..util import probar_conexion

uiFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dlg_config.ui'))
DIALOG_UI = uic.loadUiType(uiFilePath)[0]


class ConfigDialog(QDialog, DIALOG_UI):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        s = QgsSettings()
        self.linePgRemotoHost.setText(s.value("SerEIEL/pgremoto_host", "ortho4"))
        self.linePgRemotoPuerto.setText(s.value("SerEIEL/pgremoto_puerto", "5432"))
        self.linePgRemotoBBDD.setText(s.value("SerEIEL/pgremoto_bbdd", "eiel_zamora"))
        self.linePgRemotoUsuario.setText(s.value("SerEIEL/pgremoto_usuario", "postgres"))
        self.linePgRemotoPassword.setText(s.value("SerEIEL/pgremoto_password", "Seresco_2000"))

        self.linePgLocalHost.setText(s.value("SerEIEL/pglocal_host", "localhost"))
        self.linePgLocalPuerto.setText(s.value("SerEIEL/pglocal_puerto", "5433"))
        self.linePgLocalBBDD.setText(s.value("SerEIEL/pglocal_bbdd", "eiel_zamora"))
        self.linePgLocalUsuario.setText(s.value("SerEIEL/pglocal_usuario", "postgres"))
        self.linePgLocalPassword.setText(s.value("SerEIEL/pglocal_password", "Seresco_2000"))

        self.lineFase.setText(s.value("SerEIEL/fase", "2016"))
        self.lineRutaSalida.setText(s.value("SerEIEL/ruta_exportacion", ""))

        self.parent = parent
        self.botonGuardar.clicked.connect(self.guardar_configuracion)
        self.pushProbarConexionServidor.clicked.connect(self.probar_conexion_servidor)
        self.pushProbarConexionLocal.clicked.connect(self.probar_conexion_local)

    def probar_conexion_servidor(self):
        s = QgsSettings()
        probar_conexion(self.linePgRemotoHost.text(), self.linePgRemotoPuerto.text(),
                        self.linePgRemotoBBDD.text(), self.linePgRemotoUsuario.text(),
                        self.linePgRemotoPassword.text())

    def probar_conexion_local(self):
        s = QgsSettings()
        probar_conexion(self.linePgLocalHost.text(), self.linePgLocalPuerto.text(),
                        self.linePgLocalBBDD.text(), self.linePgLocalUsuario.text(),
                        self.linePgLocalPassword.text())

    def guardar_configuracion(self):
        s = QgsSettings()
        s.setValue("SerEIEL/pgremoto_host", self.linePgRemotoHost.text())
        s.setValue("SerEIEL/pgremoto_puerto", self.linePgRemotoPuerto.text())
        s.setValue("SerEIEL/pgremoto_bbdd", self.linePgRemotoBBDD.text())
        s.setValue("SerEIEL/pgremoto_usuario", self.linePgRemotoUsuario.text())
        s.setValue("SerEIEL/pgremoto_password", self.linePgRemotoPassword.text())

        s.setValue("SerEIEL/pglocal_host", self.linePgLocalHost.text())
        s.setValue("SerEIEL/pglocal_puerto", self.linePgLocalPuerto.text())
        s.setValue("SerEIEL/pglocal_bbdd", self.linePgLocalBBDD.text())
        s.setValue("SerEIEL/pglocal_usuario", self.linePgLocalUsuario.text())
        s.setValue("SerEIEL/pglocal_password", self.linePgLocalPassword.text())

        s.setValue("SerEIEL/fase", self.lineFase.text())
        s.setValue("SerEIEL/ruta_exportacion", self.lineRutaSalida.text())

        iface.messageBar().pushMessage("SerEIEL", "Configuración guardada correctamente", level=Qgis.Success)
        self.close()
