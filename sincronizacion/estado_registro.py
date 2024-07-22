from qgis._core import QgsMessageLog, Qgis

from .estado import Estado


class EstadoRegistro:
    
    def __init__(self, registro: dict):
        self._registro = registro
        self._estado = Estado.Original
        self._fecha_mod = registro['ser_fecha_mod']
        self._diferencias = []
        if self._fecha_mod is not None:
            self._estado = Estado.Modificado
        self._uuid = registro['ser_uuid']
        
    def comparar(self, eregistro_comp):
        self._diferencias = []
        # QgsMessageLog.logMessage('Comparando:', 'SerEIEL', Qgis.Info)
        # QgsMessageLog.logMessage(str(self._registro), 'SerEIEL', Qgis.Info)
        # QgsMessageLog.logMessage('Y:', 'SerEIEL', Qgis.Info)
        # QgsMessageLog.logMessage(str(row_comp), 'SerEIEL', Qgis.Info)
        for key in self._registro.keys():
            # QgsMessageLog.logMessage('Campo ' + key, 'SerEIEL', Qgis.Info)
            if key.lower().startswith('ser_') or key.lower() == 'idx':
                # QgsMessageLog.logMessage('-- Ignorar', 'SerEIEL', Qgis.Info)
                continue
            if key not in eregistro_comp.registro:
                # QgsMessageLog.logMessage('-- No existe en el otro registro', 'SerEIEL', Qgis.Info)
                continue
            if self._registro[key] != eregistro_comp.registro[key]:
                # QgsMessageLog.logMessage('-- Distinto valor!! (%s) -> (%s)' % (self._registro[key], row_comp[key]), 'SerEIEL', Qgis.Info)
                self._diferencias.append((key, self._registro[key], eregistro_comp.registro[key]))
            # else:
            #     QgsMessageLog.logMessage('-- Mismo valor', 'SerEIEL', Qgis.Info)
        if len(self._diferencias) > 0:
            self._estado = Estado.Modificado
            if eregistro_comp.estado == Estado.Modificado:
                self._estado = Estado.ConflictoModificados
                eregistro_comp.estado = Estado.ConflictoModificados
        else:
            self._estado = Estado.Original
            eregistro_comp.estado = Estado.Original
                
    @property
    def registro(self):
        return self._registro
    
    @registro.setter
    def registro(self, value):
        self._registro = value
        
    @property
    def diferencias(self):
        return self._diferencias
    
    @diferencias.setter
    def diferencias(self, value):
        self._diferencias = value
        
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, value):
        self._estado = value
    
    @property
    def fecha_mod(self):
        return self._fecha_mod
    
    @fecha_mod.setter
    def fecha_mod(self, value):
        self._fecha_mod = value
        if value is not None and self._estado == Estado.Original:
            self._estado = Estado.Modificado
        elif value is None and self._estado == Estado.Modificado:
            self._estado = Estado.Original
    
    @property
    def uuid(self):
        return self._uuid
    
    @uuid.setter
    def uuid(self, value):
        self._uuid = value
        
    def __str__(self):
        return str(self._uuid) + " || " + str(self._fecha_mod) + " ||  " + str(self._estado)
    
    def __repr__(self):
        return str(self._uuid) + " || " + str(self._fecha_mod) + " ||  " + str(self._estado)
