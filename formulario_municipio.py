# -*- codificación: utf-8 -*-
from qgis.PyQt.QtWidgets import QWidget
from qgis.utils import iface


def preparar_botones_formulario(dialog, layer, feature):
    
    campos_tabla_actual = ['fase', 'provincia', 'municipio']
    
    def crear_filtro(camposOrigen, camposDestino):
        plantilla = '"%s" = \'%s\''
        condiciones = []
        for i in range(len(camposOrigen)):
            condiciones.append(plantilla % (camposDestino[i], feature[camposOrigen[i]]))
        return ' and '.join(condiciones)
    
    def mostrar_tabla_filtrada(tabla, campos):
        capas = QgsProject.instance().mapLayersByName(tabla)
        if len(capas) == 0:
            iface.messageBar().pushMessage("SerEIEL", "No se encontró la capa " + tabla, level=Qgis.Warning)
            return
        attDialog = iface.showAttributeTable(capas[0], crear_filtro(campos_tabla_actual, campos))
    
    def conectar_boton(nombre_boton, tabla, campos):
        boton = dialog.findChild(QWidget, nombre_boton)
        if boton is None:
            iface.messageBar().pushMessage("SerEIEL", "No se encontró el botón " + nombre_boton, level=Qgis.Warning)
            return
        boton.disconnect()
        boton.clicked.connect(lambda: mostrar_tabla_filtrada(tabla, campos))

    # -*- Abastecimiento -*-
    conectar_boton("botonNucleo2", 'nucl_encuestado_2', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonNucleo3", 'nucl_encuestado_3', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonNucleo4", 'nucl_encuestado_4', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonDepositos", 'deposito_enc', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCaptaciones", 'captacion_enc', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonConducciones", 'tramo_conduccion', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonPotabilizadoras", 'potabilizacion_enc', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonReddist", 'red_distribucion', ['fase', 'provincia', 'municipio'])
    # -*- Saneamiento -*-
    conectar_boton("botonNucleo5", 'nucl_encuestado_5', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonDepuradoras", 'depuradora_enc', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonColectores", 'tramo_colector', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonTramoemi", 'tramo_emisario', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonRamalsan", 'ramal_saneamiento', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonSaneaauto", 'sanea_autonomo', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonPtovertido", 'punto_vertido', ['fase', 'provincia', 'municipio'])
    # -*- Equipamientos -*-
    conectar_boton("botonCasasConsist", 'casa_consistorial', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCementerios", 'cementerio', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCentrosAsistenciales", 'centro_asistencial', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCentrosCulturales", 'cent_cultural', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCentrosEnsenanza", 'centro_ensenanza', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCentrosSanitarios", 'centro_sanitario', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonEdificiosSinUso", 'edific_pub_sin_uso', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonInslalacionesDeportivas", 'instal_deportiva', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonLMF", 'lonja_merc_feria', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonMataderos", 'matadero', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonParques", 'parque', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonProteccionCivil", 'proteccion_civil', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonTanatorios", 'tanatorio', ['fase', 'provincia', 'municipio'])
    # -*- Alumbrado -*-
    conectar_boton("botonAlumbrado", 'alumbrado', ['fase', 'provincia', 'municipio'])
    # -*- General -*-
    conectar_boton("botonNucleo1", 'nucl_encuestado_1', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonNucleo7", 'nucl_encuestado_7', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCabildo", 'cabildo_consejo', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonEntsing", 'entidad_singular', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonNucleoaban", 'nuc_abandonado', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonMundis", 'munc_enc_dis', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonOtserv", 'ot_serv_municipal', ['fase', 'provincia', 'municipio'])
    # -*- Red de Transportes -*-
    conectar_boton("botonInfViaria", 'infraestr_viaria', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCarreteras", 'tramo_carretera', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonCalleslin", 'calles_lineales', ['fase', 'provincia', 'municipio'])
    # -*- Residuos -*-
    conectar_boton("botonBasuras", 'recogida_basura', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonVertederos", 'vert_encuestado', ['fase', 'provincia', 'municipio'])
    conectar_boton("botonNucleo6", 'nucl_encuestado_6', ['fase', 'provincia', 'municipio'])
    # -*- Anotaciones -*-
    conectar_boton("botonComentarios", 'SER_anotaciones', ['fase', 'provincia', 'municipio'])