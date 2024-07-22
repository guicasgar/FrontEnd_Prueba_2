# def exportar_txt(self, progressbar, directorio_salida, nombre, sql):
#     try:
#         self.valor += 1
#         progressbar.setFormat('Exportando {}...'.format(nombre))
#         progressbar.setValue(self.valor * 100 / self.total)
#         ds = gdal.VectorTranslate(
#             destNameOrDestDS=directorio_salida + "/" + nombre + ".csv",
#             srcDS="PG:dbname=eiel_zamora host=eielzamora port=5432 user=postgres password=admin@985",
#             format="CSV",
#             SQLStatement=sql
#         )
#     except Exception as e:
#         print(f"Translation failed: {e}")


# ---------------------------------------------ALIVIADERO----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "aliviadero",
#      """select geom, '2020' as "FASE", clave "CLAVE", prov "PROV", mun "MUN", ent "ENT", nucleo "NUCLEO"
#      from eiel.aliviadero a
#      order by fase , clave , prov , mun , ent , nucleo""")
#
#
#         # ---------------------------------------------ALUMBRADO----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "alumbrado",
#      """select geom, '2020' as "FASE", provincia "PROV", municipio "MUN", entidad "ENT", nucleo "NUCLEO", ah_ener_rl "AH_ENER_RL", ah_ener_ri "AH_ENER_RI", calidad "CALIDAD"
#      from eiel.alumbrado a
#      order by fase , provincia , municipio , entidad , nucleo , ah_ener_rl , ah_ener_ri , calidad""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "ALUMBRADO",
#     """select distinct '2020' as fase, provincia, municipio , entidad , nucleo , ah_ener_rl , ah_ener_ri , calidad, pot_instal , puntos_luz
#     from eiel.alumbrado a
#     order by fase, provincia, municipio , entidad , nucleo , ah_ener_rl , ah_ener_ri , calidad, pot_instal , puntos_luz""")
#
#
#         # ---------------------------------------------CABILDO_CONSEJO----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CABILDO_CONSEJO", """select '2020' as fase , provincia , isla , denominaci
#     from eiel.cabildo_consejo cc
#     order by fase , provincia , isla , denominaci""")
#
#         #---------------------------------------------CAPTACION_ENC----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "captacion_enc", """select geom, '2020' as "FASE", upper(clave) "CLAVE", provincia "PROV", municipio "MUN", orden_capt "ORDEN_CAPT"
#     from eiel.captacion_enc ce
#     where municipio != '275'
#     order by fase, upper(clave), provincia, municipio , orden_capt""")
#         self.exportar_shape(progressbar, directorio_salida, "captacion_enc_m50", """select geom, '2020' as "FASE", clave "CLAVE", provincia "PROV", municipio "MUN", orden_capt "ORDEN_CAPT"
#     from eiel.captacion_enc ce
#     where municipio = '275'
#     order by fase, clave, provincia, municipio , orden_capt """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CAPTACION_AGUA", """select '2020' as fase , clave , provincia , municipio , orden_capt
#     from eiel.captacion_enc ce
#     order by fase, clave, provincia, municipio , orden_capt""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CAPTACION_ENC", """select distinct
#     '2020' as fase, clave, provincia, municipio, orden_capt, denominaci, tipo_capt , titular , gestion , sistema_ca , estado , uso, proteccion , contador
#     from eiel.captacion_enc ce
#     where municipio != '275'
#     order by fase, clave, provincia, municipio, orden_capt, denominaci, tipo_capt , titular , gestion , sistema_ca , estado , uso, proteccion , contador""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CAPTACION_ENC_M50", """select distinct
#     '2020' as fase, clave, provincia, municipio, orden_capt, denominaci, tipo_capt , titular , gestion , sistema_ca , estado , uso, proteccion , contador
#     from eiel.captacion_enc ce
#     where municipio = '275'
#     order by fase, clave, provincia, municipio, orden_capt, denominaci, tipo_capt , titular , gestion , sistema_ca , estado , uso, proteccion , contador""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CAP_AGUA_NUCLEO", """select
#     '2020' as fase, serv_pro, serv_mun , serv_ent , serv_nucle , clave , c_provinc , c_municip , orden_capt
#     from eiel.cap_agua_nucleo can
#     where exists
#     (select 1 from eiel.captacion_enc ce
#     where can.fase = ce.fase and can.serv_mun = ce.municipio and can.clave = ce.clave and can.c_provinc = ce.provincia and can.orden_capt = ce.orden_capt)""")
#
#         # ---------------------------------------------CASA_CONSISTORIAL----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "casa_consistorial",
#     """select geom , '2020' as "FASE", clave "CLAVE", provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_casa "ORDEN_CASA"
#     from eiel.casa_consistorial cc
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_casa""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CASA_CONSISTORIAL",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_casa , nombre , tipo , titular , tenencia , s_cubi , s_aire , s_sola , acceso_s_r , estado
#     from eiel.casa_consistorial cc
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_casa , nombre , tipo , titular , tenencia , s_cubi , s_aire , s_sola , acceso_s_r , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CASA_CON_USO", """select '2020' as fase, clave, provincia, municipio, entidad, poblamient, orden_casa, uso, s_cubi
#     from eiel.casa_con_uso ccu
#     where exists
#     (select 1 from eiel.casa_consistorial cc
#     where cc.fase = ccu.fase and cc.clave = ccu.clave and cc.provincia = ccu.provincia and cc.municipio = ccu.municipio and
#     cc.entidad = ccu.entidad and cc.poblamient = ccu.poblamient and cc.orden_casa = ccu.orden_casa)""")
#
#         # ----------------------------------------------CEMENTERIO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "cementerio",
#     """select geom , '2020' as "FASE" ,clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_ceme "ORDEN_CEME"
#     from eiel.cementerio c
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_ceme""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CEMENTERIO",
#     """select
#     '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_ceme , nombre , titular , distancia , acceso , capilla , deposito , ampliacion , saturacion , superficie , acceso_s_r , crematorio
#     from eiel.cementerio c
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_ceme , nombre , titular , distancia , acceso , capilla , deposito , ampliacion , saturacion , superficie , acceso_s_r , crematorio
#     """)
#
#         # ----------------------------------------------CENTRO_CULTURAL-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "centro_cultural", """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_cent "ORDEN_CENT"
#     from eiel.cent_cultural cc
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_cent""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CENT_CULTURAL",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_cent , nombre , tipo_cent , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado
#     from eiel.cent_cultural cc
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_cent , nombre , tipo_cent , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CENT_CULTURAL_USOS",
#     """select '2020' as fase, clave, provincia, municipio, entidad, poblamient, orden_cent, uso, s_cubi
#     from eiel.cent_cultural_usos ccu
#     where exists
#     (select 1 from eiel.cent_cultural cc2
#     where ccu.fase = cc2.fase and ccu.clave = cc2.clave and ccu.provincia = cc2.provincia and ccu.municipio = cc2.municipio and
#     ccu.entidad = cc2.entidad and ccu.poblamient = cc2.poblamient and ccu.orden_cent = cc2.orden_cent)""")
#
#         # ----------------------------------------------CENTRO_ASISTENCIAL-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "centro_asistencial",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_casi "ORDEN_CASI"
#     from eiel.centro_asistencial ca
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_casi """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CENTRO_ASISTENCIAL",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_casi , nombre , tipo_casis , titular , gestion , plazas , s_cubi , s_aire , s_sola , acceso_s_r , estado
#     from eiel.centro_asistencial ca
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_casi , nombre , tipo_casis , titular , gestion , plazas , s_cubi , s_aire , s_sola , acceso_s_r , estado""")
#
#         # ----------------------------------------------CENTRO_ENSEÑANZA-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "centro_ensenanza",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_cent "ORDEN_CENT"
#     from eiel.centro_ensenanza ce
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_cent""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CENTRO_ENSENANZA",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_cent , nombre , ambito , titular , s_cubi , s_aire , s_sola , acceso_s_r , estado
#     from eiel.centro_ensenanza ce
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_cent , nombre , ambito , titular , s_cubi , s_aire , s_sola , acceso_s_r , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NIVEL_ENSENANZA",
#     """select '2020' as fase, clave, provincia, municipio, entidad, poblamient, orden_cent, nivel
#     from eiel.nivel_ensenanza ne
#     where exists
#     (select 1 from eiel.centro_ensenanza ce
#     where ne.fase = ce.fase and ne.clave = ce.clave and ne.provincia = ce.provincia and ne.municipio = ce.municipio and
#     ne.entidad = ce.entidad and ne.poblamient = ce.poblamient and ne.orden_cent = ce.orden_cent)""")
#
#         # ----------------------------------------------CENTRO_SANITARIO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "centro_sanitario",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_csan "ORDEN_CSAN"
#     from eiel.centro_sanitario cs
#     order by fase, clave, provincia , municipio , entidad , poblamient , orden_csan""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CENTRO_SANITARIO",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_csan , nombre , tipo_csan , titular , gestion , s_cubi , s_aire , s_sola , uci , camas , acceso_s_r , estado
#     from eiel.centro_sanitario cs
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_csan , nombre , tipo_csan , titular , gestion , s_cubi , s_aire , s_sola , uci , camas , acceso_s_r , estado""")
#
#         # ---------------------------------------------DEPOSITO_ENC----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "deposito_enc",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_depo "ORDEN_DEPO"
#     from eiel.deposito_enc de
#     where municipio != '275'
#     order by fase, clave, provincia, municipio, orden_depo""")
#         self.exportar_shape(progressbar, directorio_salida, "deposito_enc_m50",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_depo "ORDEN_DEPO"
#     from eiel.deposito_enc de
#     where municipio = '275'
#     order by fase, clave, provincia, municipio, orden_depo""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPOSITO",
#     """select '2020' as fase , clave , provincia , municipio , orden_depo
#     from eiel.deposito_enc de
#     order by fase, clave, provincia, municipio, orden_depo""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPOSITO_ENC",
#     """select '2020' as fase , clave , provincia , municipio , orden_depo , ubicacion , titular , gestion , capacidad , estado , proteccion , limpieza, contador
#     from eiel.deposito_enc de
#     where municipio != '275'
#     order by fase, clave, provincia, municipio, orden_depo , ubicacion , titular , gestion , capacidad , estado , proteccion , limpieza, contador""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPOSITO_ENC_M50",
#     """select '2020' as fase , clave , provincia , municipio , orden_depo , ubicacion , titular , gestion , capacidad , estado , proteccion , limpieza, contador
#     from eiel.deposito_enc de
#     where municipio = '275'
#     order by fase, clave, provincia, municipio, orden_depo , ubicacion , titular , gestion , capacidad , estado , proteccion , limpieza, contador""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPOSITO_AGUA_NUCLEO",
#     """select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , de_provinc , de_municip , orden_depo
#     from eiel.deposito_agua_nucleo dan
#     where exists
#     (select 1 from eiel.deposito_enc de
#     where dan.fase = de.fase and dan.serv_pro = de.provincia and dan.serv_mun = de.municipio and dan.clave = de.clave and dan.orden_depo = de.orden_depo)""")
#
#         # ---------------------------------------------DEPURADORA----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "depuradora_enc", """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_depu "ORDEN_DEPU"
#     from eiel.depuradora_enc de
#     where municipio != '275'
#     order by fase, clave, provincia, municipio, orden_depu""")
#         self.exportar_shape(progressbar, directorio_salida, "depuradora_enc_m50", """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_depu "ORDEN_DEPU"
#     from eiel.depuradora_enc de
#     where municipio = '275'
#     order by fase, clave, provincia, municipio, orden_depu""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPURADORA", """select '2020' as fase, clave , provincia , municipio , orden_depu
#     from eiel.depuradora_enc de
#     order by fase, clave , provincia , municipio , orden_depu""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPURADORA_ENC",
#     """select
#     '2020' as fase , clave , provincia , municipio , orden_depu , trat_pr_1 , trat_pr_2 , trat_pr_3 , trat_sc_1 , trat_sc_2 , trat_sc_3 , trat_av_1 , trat_av_2 , trat_av_3 , proc_cm_1 , proc_cm_2 , proc_cm_3 , trat_ld_1 , trat_ld_2 , trat_ld_3
#     from eiel.depuradora_enc de
#     where municipio != '275'
#     order by fase, clave, provincia, municipio, orden_depu , trat_pr_1 , trat_pr_2 , trat_pr_3 , trat_sc_1 , trat_sc_2 , trat_sc_3 , trat_av_1 , trat_av_2 , trat_av_3 , proc_cm_1 , proc_cm_2 , proc_cm_3 , trat_ld_1 , trat_ld_2 , trat_ld_3
#     """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPURADORA_ENC_2",
#     """select '2020' as fase , clave , provincia , municipio , orden_depu , titular , gestion , capacidad , problem_1 , problem_2 , problem_3 , lodo_gest , lodo_vert , lodo_inci , lodo_con_a , lodo_sin_a , lodo_ot
#     from eiel.depuradora_enc de
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_depu , titular , gestion , capacidad , problem_1 , problem_2 , problem_3 , lodo_gest , lodo_vert , lodo_inci , lodo_con_a , lodo_sin_a , lodo_ot""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPURADORA_ENC_M50",
#     """select
#     '2020' as fase , clave , provincia , municipio , orden_depu , trat_pr_1 , trat_pr_2 , trat_pr_3 , trat_sc_1 , trat_sc_2 , trat_sc_3 , trat_av_1 , trat_av_2 , trat_av_3 , proc_cm_1 , proc_cm_2 , proc_cm_3 , trat_ld_1 , trat_ld_2 , trat_ld_3
#     from eiel.depuradora_enc de
#     where municipio = '275'
#     order by fase, clave, provincia, municipio, orden_depu , trat_pr_1 , trat_pr_2 , trat_pr_3 , trat_sc_1 , trat_sc_2 , trat_sc_3 , trat_av_1 , trat_av_2 , trat_av_3 , proc_cm_1 , proc_cm_2 , proc_cm_3 , trat_ld_1 , trat_ld_2 , trat_ld_3
#     """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEPURADORA_ENC_2_M50",
#     """select '2020' as fase , clave , provincia , municipio , orden_depu , titular , gestion , capacidad , problem_1 , problem_2 , problem_3 , lodo_gest , lodo_vert , lodo_inci , lodo_con_a , lodo_sin_a , lodo_ot
#     from eiel.depuradora_enc de
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_depu , titular , gestion , capacidad , problem_1 , problem_2 , problem_3 , lodo_gest , lodo_vert , lodo_inci , lodo_con_a , lodo_sin_a , lodo_ot""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "DEP_AGUA_NUCLEO",
#     """select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , de_provinc , de_municip , orden_depu
#     from eiel.depuradora_agua_nucleo dan
#     where exists
#     (select 1 from eiel.depuradora_enc de
#     where dan.fase = de.fase and dan.serv_pro = de.provincia and dan.serv_mun = de.municipio and dan.clave = de.clave and dan.orden_depu = de.orden_depu)""")
#
#         # ----------------------------------------------ENTIDAD_SINGULAR-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "ENTIDAD_SINGULAR",
#     """select '2020' as fase , provincia , municipio , entidad , denominaci
#     from eiel.entidad_singular es
#     order by fase , provincia , municipio , entidad , denominaci""")
#
#         # ----------------------------------------------EDIFIC_PUB_SIN_USO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "edific_pub_sin_uso",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENTIDAD" , poblamient "POBLAMIENT" , orden_edif "ORDEN_EDIF"
#     from eiel.edific_pub_sin_uso epsu
#     order by fase, clave, provincia , municipio , entidad ,  poblamient , orden_edif""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "EDIFIC_PUB_SIN_USO",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_edif , nombre , titular , s_cubi , s_aire , s_sola , estado , usoant
#     from eiel.edific_pub_sin_uso epsu
#     order by fase, clave, provincia , municipio , entidad , poblamient , orden_edif , nombre , titular , s_cubi , s_aire , s_sola , estado , usoant""")
#
#         # ---------------------------------------------PUNTO_VERTIDO----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "punto_vertido", """select geom , '2020' as "FASE" , clave "CLAVE" , prov "PROV" , mun "MUN" , orden_emis "ORDEN_EMIS"
#     from eiel.punto_vertido pv
#     where mun != '275'
#     order by fase , clave , prov , mun , orden_emis """)
#         self.exportar_shape(progressbar, directorio_salida, "punto_vertido_m50", """select geom , '2020' as "FASE" , clave "CLAVE" , prov "PROV" , mun "MUN" , orden_emis "ORDEN_EMIS"
#     from eiel.punto_vertido pv
#     where mun = '275'
#     order by fase , clave , prov , mun , orden_emis""")
# #         self.exportar_txt(self.con, progressbar, directorio_salida, "PUNTO_VERTIDO", """select fase , clave , prov , mun , orden_emis , tipo_vert , zona_vert , distancia
# # from eiel.punto_vertido pv
# # where mun != '275'
# # order by fase , clave , prov , mun , orden_emis , tipo_vert , zona_vert , distancia""")
# #         self.exportar_txt(self.con, progressbar, directorio_salida, "PUNTO_VERTIDO_M50", """select fase , clave , prov , mun , orden_emis , tipo_vert , zona_vert , distancia
# # from eiel.punto_vertido pv
# # where mun = '275'
# # order by fase , clave , prov , mun , orden_emis , tipo_vert , zona_vert , distancia""")
#
#         # ----------------------------------------------INFRAESTR_VIARIA-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "infraestr_viaria",
#     """select geom , '2020' as "FASE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , nucleo "NUCLEO" , tipo_infr "TIPO_INFR" , estado "ESTADO"
#     from eiel.infraestr_viaria iv
#     order by fase , provincia , municipio , entidad , nucleo , tipo_infr , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "INFRAESTR_VIARIA",
#     """select distinct '2020' as fase , provincia , municipio , entidad , nucleo , tipo_infr , estado, longitud , superficie , viv_afecta
#     from eiel.infraestr_viaria iv
#     order by fase , provincia , municipio , entidad , nucleo , tipo_infr , estado , longitud , superficie , viv_afecta""")
#
#         # ----------------------------------------------INSTAL_DEPORTIVA-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "instal_deportiva",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_inst "ORDEN_INST"
#     from eiel.instal_deportiva id
#     order by fase, clave, provincia , municipio , entidad ,  poblamient , orden_inst , nombre , tipo_insde , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "INSTAL_DEPORTIVA",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_inst , nombre , tipo_insde , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado
#     from eiel.instal_deportiva id
#     order by fase, clave, provincia , municipio , entidad ,  poblamient , orden_inst , nombre , tipo_insde , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "INST_DEPOR_DEPORTE",
#     """select '2020' as fase, clave, provincia, municipio, entidad, poblamient, orden_inst , tipo_depor
#     from eiel.inst_depor_deporte idd
#     where exists
#     (select 1 from eiel.instal_deportiva id
#     where idd.fase = id.fase and idd.clave = id.clave and idd.provincia = id.provincia and idd.municipio = id.municipio and
#     idd.entidad = id.entidad and idd.poblamient = id.poblamient and idd.orden_inst = id.orden_inst)""")
#
#         # ----------------------------------------------LONJA_MERC_FERIA-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "lonja_merc_feria",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_lmf "ORDEN_LMF"
#     from eiel.lonja_merc_feria lmf
#     order by fase, clave , provincia , municipio , entidad , poblamient , orden_lmf""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "LONJA_MERC_FERIA",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_lmf , nombre , tipo_lonj , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado
#     from eiel.lonja_merc_feria lmf
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_lmf , nombre , tipo_lonj , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado""")
#
#         # ----------------------------------------------MATADERO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "matadero",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_mata "ORDEN_MATA"
#     from eiel.matadero m
#     order by fase, clave , provincia , municipio , entidad , poblamient , orden_mata""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "MATADERO",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_mata , nombre , clase_mat , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado , capacidad , utilizacio , tunel , bovino , ovino , porcino , otros
#     from eiel.matadero m
#     order by fase, clave , provincia , municipio , entidad , poblamient , orden_mata , nombre , clase_mat , titular , gestion , s_cubi , s_aire , s_sola , acceso_s_r , estado , capacidad , utilizacio , tunel , bovino , ovino , porcino , otros""")
#
#         # ----------------------------------------------MUNC_ENC_DIS-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "MUNC_ENC_DIS",
#     """select '2020' as fase , provincia , municipio , padron , pob_estaci , viv_total , hoteles , casas_rura , longitud , aag_v_cone , aag_v_ncon , aag_c_invi , aag_c_vera , aag_v_expr , aag_v_depr , aag_l_defi , aag_v_defi , aag_pr_def , aag_pe_def , aau_vivien , aau_pob_re , aau_pob_es , aau_def_vi , aau_def_re , aau_def_es , aau_fecont , aau_fencon , longit_ram , syd_v_cone , syd_v_ncon , syd_l_defi , syd_v_defi , syd_pr_def , syd_pe_def , syd_c_desa , syd_c_trat , sau_vivien , sau_pob_re , sau_pob_es , sau_vi_def , sau_re_def , sau_es_def , produ_basu , contenedor , rba_v_sser , rba_pr_sse , rba_pe_sse , rba_plalim , puntos_luz , alu_v_sin , alu_l_sin
#     from eiel.munc_enc_dis med
#     order by fase , provincia , municipio , padron , pob_estaci , viv_total , hoteles , casas_rura , longitud , aag_v_cone , aag_v_ncon , aag_c_invi , aag_c_vera , aag_v_expr , aag_v_depr , aag_l_defi , aag_v_defi , aag_pr_def , aag_pe_def , aau_vivien , aau_pob_re , aau_pob_es , aau_def_vi , aau_def_re , aau_def_es , aau_fecont , aau_fencon , longit_ram , syd_v_cone , syd_v_ncon , syd_l_defi , syd_v_defi , syd_pr_def , syd_pe_def , syd_c_desa , syd_c_trat , sau_vivien , sau_pob_re , sau_pob_es , sau_vi_def , sau_re_def , sau_es_def , produ_basu , contenedor , rba_v_sser , rba_pr_sse , rba_pe_sse , rba_plalim , puntos_luz , alu_v_sin , alu_l_sin
#     """)
#
#         # ----------------------------------------------MUNCICPIO-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "MUNICIPIO",
#     """select '2020' as fase , provincia , municipio , isla , denominaci
#     from eiel.municipio m
#     order by fase , provincia , municipio , isla , denominaci""")
#
#         # ----------------------------------------------NUC_ABANDONADO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "nuc_abandonado",
#     """select geom , '2020' as "fase" , provincia "prov" , municipio "mun" , entidad "ent" , poblamient "poblamient"
#     from eiel.nuc_abandonado na
#     order by fase, provincia , municipio , entidad , poblamient""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUC_ABANDONADO",
#     """select '2020' as fase , provincia , municipio , entidad , poblamient , a_abandono , causa_aban , titular_ab , rehabilita , acceso_nuc , serv_agua , serv_elect
#     from eiel.nuc_abandonado na
#     order by fase , provincia , municipio , entidad , poblamient , a_abandono , causa_aban , titular_ab , rehabilita , acceso_nuc , serv_agua , serv_elect""")
#
#         # ----------------------------------------------NUCLEOS ENCUESTADOS-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUCL_ENCUESTADO_1",
#     """select '2020' as fase , provincia , municipio , entidad , nucleo , padron , pob_estaci , altitud , viv_total , hoteles , casas_rura , accesib
#     from eiel.nucl_encuestado_1 ne
#     order by fase , provincia , municipio , entidad , nucleo , padron , pob_estaci , altitud , viv_total , hoteles , casas_rura , accesib """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUCL_ENCUESTADO_2",
#     """select '2020' as fase , provincia , municipio , entidad , nucleo , aag_caudal , aag_restri , aag_contad , aag_tasa , aag_instal , aag_hidran , replace(aag_est_hi, '99', '') , aag_valvul , aag_est_va , aag_bocasr , aag_est_bo , cisterna
#     from eiel.nucl_encuestado_2 ne
#     order by fase , provincia , municipio , entidad , nucleo , aag_caudal , aag_restri , aag_contad , aag_tasa , aag_instal , aag_hidran , aag_est_hi , aag_valvul , aag_est_va , aag_bocasr , aag_est_bo , cisterna
#     """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUCL_ENCUESTADO_3",
#     """select '2020' as fase , provincia , municipio , entidad , nucleo , aag_v_cone , aag_v_ncon , aag_c_invi , aag_c_vera , aag_v_expr , aag_v_depr , aag_perdid , aag_calida , aag_l_defi , aag_v_defi , aag_pr_def , aag_pe_def
#     from eiel.nucl_encuestado_3 ne
#     order by fase , provincia , municipio , entidad , nucleo , aag_v_cone , aag_v_ncon , aag_c_invi , aag_c_vera , aag_v_expr , aag_v_depr , aag_perdid , aag_calida , aag_l_defi , aag_v_defi , aag_pr_def , aag_pe_def
#     """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUCL_ENCUESTADO_4",
#     """select '2020' as fase , provincia , municipio , entidad , nucleo , aau_vivien , aau_pob_re , aau_pob_es , aau_def_vi , aau_def_re , aau_def_es , aau_fecont , aau_fencon , aau_caudal
#     from eiel.nucl_encuestado_4 ne
#     order by fase , provincia , municipio , entidad , nucleo , aau_vivien , aau_pob_re , aau_pob_es , aau_def_vi , aau_def_re , aau_def_es , aau_fecont , aau_fencon , aau_caudal
#     """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUCL_ENCUESTADO_5",
#     """select '2020' as fase , provincia , municipio , entidad , nucleo , syd_pozos , syd_sumide , syd_ali_co , syd_ali_si , syd_calida , syd_v_cone , syd_v_ncon , syd_l_defi , syd_v_defi , syd_pr_def , syd_pe_def , syd_c_desa , syd_c_trat , syd_re_urb , syd_re_rus , syd_re_ind
#     from eiel.nucl_encuestado_5 ne
#     order by fase , provincia , municipio , entidad , nucleo , syd_pozos , syd_sumide , syd_ali_co , syd_ali_si , syd_calida , syd_v_cone , syd_v_ncon , syd_l_defi , syd_v_defi , syd_pr_def , syd_pe_def , syd_c_desa , syd_c_trat , syd_re_urb , syd_re_rus , syd_re_ind
#     """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUCL_ENCUESTADO_6",
#     """select '2020' as fase , provincia , municipio , entidad , nucleo , rba_v_sser , rba_pr_sse , rba_pe_sse , rba_serlim , rba_plalim
#     from eiel.nucl_encuestado_6 ne
#     order by fase , provincia , municipio , entidad , nucleo , rba_v_sser , rba_pr_sse , rba_pe_sse , rba_serlim , rba_plalim""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUCL_ENCUESTADO_7",
#     """select '2020' as fase , provincia , municipio , entidad , nucleo , tv_ant , tv_ca , tm_gsm , tm_umts , tm_gprs , correo , ba_rd , ba_xd , ba_wi , ba_ca , ba_rb , ba_st , capi , electricid , gas , alu_v_sin , alu_l_sin
#     from eiel.nucl_encuestado_7 ne
#     order by fase , provincia , municipio , entidad , nucleo , tv_ant , tv_ca , tm_gsm , tm_umts , tm_gprs , correo , ba_rd , ba_xd , ba_wi , ba_ca , ba_rb , ba_st , capi , electricid , gas , alu_v_sin , alu_l_sin
#     """)
#
#         # ----------------------------------------------NUCLEO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "nucleo",
#     """select geom , '2020' as "FASE" , prov "PROV" , mun "MUN" , ent "ENT" , nucleo "NUCLEO"
#     from eiel.nucleo n
#     order by fase , prov , mun , ent , nucleo""")
#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "NUCLEO_POBLACION",
#     """select '2020' as fase , prov , mun , ent , nucleo , denominaci
#     from eiel.nucleo n
#     order by fase , prov , mun , ent , nucleo , denominaci""")
#
#         # ---------------------------------------------OT_SERV_MUNICIPAL-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "OT_SERV_MUNICIPAL",
#     """select '2020' as fase , provincia , municipio , sw_inf_grl , sw_inf_tur , sw_gb_elec , ord_soterr , en_eolica , kw_eolica , en_solar , kw_solar , pl_mareo , kw_mareo , ot_energ , kw_energ , cob_serv_t , tv_dig_cab
#     from eiel.ot_serv_municipal osm
#     order by fase , provincia , municipio , sw_inf_grl , sw_inf_tur , sw_gb_elec , ord_soterr , en_eolica , kw_eolica , en_solar , kw_solar , pl_mareo , kw_mareo , ot_energ , kw_energ , cob_serv_t , tv_dig_cab
#     """)
#
#         # ---------------------------------------------PADRON-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "PADRON",
#     """select fase , provincia , municipio , hombres , mujeres , poblacion_total
#     from eiel.padron p
#     order by fase , provincia , municipio , hombres , mujeres , poblacion_total """)
#
#         # ----------------------------------------------ZONAS_NATURALES-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "zonas_naturales", """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_parq "ORDEN_PARQ"
#     from eiel.parque p
#     where tipo_parq = 'AN'
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_parq""")
#
#         self.exportar_shape(progressbar, directorio_salida, "parque", """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_parq "ORDEN_PARQ"
#     from eiel.parque p
#     where tipo_parq != 'AN'
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_parq""")
#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "PARQUE", """select '2020' as fase , clave , provincia , municipio , entidad , poblamient  , orden_parq , nombre , tipo_parq , titular , gestion , s_cubi , s_aire , s_sola , agua , saneamient , electricid , comedor , juegos_inf , otras , acceso_s_r , estado
#     from eiel.parque p
#     where tipo_parq != 'AN'
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_parq , nombre , tipo_parq , titular , gestion , s_cubi , s_aire , s_sola , agua , saneamient , electricid , comedor , juegos_inf , otras , acceso_s_r , estado""")
#
#         # -------------------------------------------PLANEAMIENTO_URBANISTICO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "suelo_rural",
#     """select geom , fase "fase" , prov "prov" , mun "mun" , tipo_urba "tipo_urba" , estado_tra "estado_tra" , denominaci "denominaci"
#     from eiel.planeamiento_urbanistico pu
#     where tipo_suelo = 'SR'
#     order by fase , prov , mun , tipo_urba , estado_tra , denominaci""")
#
#         self.exportar_shape(progressbar, directorio_salida, "suelo_urbano",
#         """select geom , fase "fase" , prov "prov" , mun "mun" , tipo_urba "tipo_urba" , estado_tra "estado_tra" , denominaci "denominaci"
#     from eiel.planeamiento_urbanistico pu
#     where tipo_suelo = 'SU'
#     order by fase , prov , mun , tipo_urba , estado_tra , denominaci""")
#
#         self.exportar_shape(progressbar, directorio_salida, "suelo_rural_preservado",
#         """select geom , fase "fase" , prov "prov" , mun "mun" , tipo_urba "tipo_urba" , estado_tra "estado_tra" , denominaci "denominaci"
#     from eiel.planeamiento_urbanistico pu
#     where tipo_suelo = 'SRP'
#     order by fase , prov , mun , tipo_urba , estado_tra , denominaci""")
#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "PLANEAMIENTO_URBANISTICO",
#     """select fase , prov , mun , tipo_urba , estado_tra , denominaci , m_superf , m_bo , urban , rural , rural_pres
#     from eiel.planeamiento_urbanistico pu
#     order by fase , prov , mun , tipo_urba , estado_tra , denominaci , m_superf , m_bo , urban , rural , rural_pres""")
#
#         # ----------------------------------------------POBLAMIENTO-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "POBLAMIENTO",
#     """select '2020' as fase , provincia , municipio , entidad , poblamient
#     from eiel.poblamiento p
#     order by fase , provincia , municipio , entidad , poblamient """)
#
#         # ----------------------------------------------PROTECCION_CIVIL-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "proteccion_civil",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_prot "ORDEN_PROT"
#     from eiel.proteccion_civil pc
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_prot""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "PROTECCION_CIVIL",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_prot , nombre , tipo_pciv , titular , gestion , ambito , plan_profe , plan_volun , s_cubi , s_aire , s_sola , acceso_s_r , estado , vehic_ince , vehic_resc , ambulancia , medios_aer , otros_vehi , quitanieve , detec_ince , otros
#     from eiel.proteccion_civil pc
#     order by
#     fase , clave , provincia , municipio , entidad , poblamient , orden_prot , nombre , tipo_pciv , titular , gestion , ambito , plan_profe , plan_volun , s_cubi , s_aire , s_sola , acceso_s_r , estado , vehic_ince , vehic_resc , ambulancia , medios_aer , otros_vehi , quitanieve , detec_ince , otros""")
#
#         # ----------------------------------------------PROVINCIA-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "PROVINCIA",
#     """select '2020' as fase , provincia , denominaci
#     from eiel.provincia p
#     order by fase , provincia , denominaci""")
#
#         # ----------------------------------------------RAMAL_SANEAMIENTO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "ramal_saneamiento",
#     """select geom , '2020' as "FASE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , nucleo "NUCLEO" , tipo_rama "TIPO_RAMA" , sist_trans "SIST_TRANS" , estado "ESTADO" , tipo_red "TIPO_RED" , titular "TITULAR" , gestion "GESTION"
#     from eiel.ramal_saneamiento rs
#     order by fase , provincia , municipio , entidad , nucleo , tipo_rama , sist_trans , estado , tipo_red , titular , gestion""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "RAMAL_SANEAMIENTO",
#     """select distinct '2020' as fase , provincia , municipio , entidad , nucleo , tipo_rama , sist_trans , estado , tipo_red , titular , gestion , longit_ram
#     from eiel.ramal_saneamiento rs
#     order by fase , provincia , municipio , entidad , nucleo , tipo_rama , sist_trans , estado , tipo_red , titular , gestion , longit_ram""")
#
#         # ----------------------------------------------RECOGIDA_BASURAS-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "RECOGIDA_BASURA",
#     """select '2020' as fase , provincia , municipio , entidad , nucleo , tipo_rbas , gestion , periodicid , calidad , produ_basu , contenedor
# from eiel.recogida_basura rb
# order by fase , provincia , municipio , entidad , nucleo , tipo_rbas , gestion , periodicid , calidad , produ_basu , contenedor""")
#
#         # ----------------------------------------------RED_DISTRIBUCION-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "red_distribucion",
#     """select geom , '2020' as "FASE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , nucleo "NUCLEO" , tipo_rdis  "TIPO_RDIS" , sist_trans "SIST_TRANS" , estado "ESTADO" , titular "TITULAR" , gestion "GESTION"
#     from eiel.red_distribucion rd
#     order by fase , provincia , municipio , entidad , nucleo , tipo_rdis , sist_trans , estado , titular , gestion""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "RED_DISTRIBUCION",
#     """select distinct '2020' as fase , provincia , municipio , entidad , nucleo , tipo_rdis , sist_trans , estado , titular , gestion , longitud
#     from eiel.red_distribucion rd
#     order by fase , provincia , municipio , entidad , nucleo , tipo_rdis , sist_trans , estado ,  titular , gestion , longitud""")
#
#         # ----------------------------------------------SANEA_AUTONOMO-----------------------------------------------------#
#         self.exportar_txt(self.con, progressbar, directorio_salida, "SANEA_AUTONOMO",
#     """select '2020' as fase , prov , mun , ent , nucleo , tipo_sanea , estado , adecuacion , sau_vivien , sau_pob_re , sau_pob_es , sau_pob_vi_def , sau_pob_re_def , sau_pob_es_def
#     from eiel.sanea_autonomo sa
#     order by fase , prov , mun , ent , nucleo , tipo_sanea , estado , adecuacion , sau_vivien , sau_pob_re , sau_pob_es , sau_pob_vi_def , sau_pob_re_def , sau_pob_es_def
#     """)
#
#         # ----------------------------------------------TANATORIO-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "tanatorio",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , entidad "ENT" , poblamient "POBLAMIENT" , orden_tana "ORDEN_TANA"
#     from eiel.tanatorio t
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_tana""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TANATORIO",
#     """select '2020' as fase , clave , provincia , municipio , entidad , poblamient , orden_tana , nombre , titular , gestion , s_cubi , s_aire , s_sola , salas , acceso_s_r , estado
#     from eiel.tanatorio t
#     order by fase , clave , provincia , municipio , entidad , poblamient , orden_tana , nombre , titular , gestion , s_cubi , s_aire , s_sola , salas , acceso_s_r , estado""")
#
#         # ---------------------------------------------POTABILIZACION_ENC----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "potabilizacion_enc", """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_trat  "ORDEN_TRAT"
#     from eiel.potabilizacion_enc pe
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_trat""")
#         self.exportar_shape(progressbar, directorio_salida, "potabilizacion_enc_m50", """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_trat  "ORDEN_TRAT"
#     from eiel.potabilizacion_enc pe
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_trat""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRA_POTABILIZACION",
#     """select '2020' as fase , clave , provincia , municipio , orden_trat
#     from eiel.potabilizacion_enc pe
#     order by fase , clave , provincia , municipio , orden_trat""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "POTABILIZACION_ENC", """select '2020' as fase , clave , provincia , municipio , orden_trat , tipo_tra , ubicacion , s_desinf , cat_a1 , cat_a2 , cat_a3 , desaladora , otros , desinf_1 , desinf_2 , desinf_3 , periodicid , organismo , estado
#     from eiel.potabilizacion_enc pe
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_trat , tipo_tra , ubicacion , s_desinf , cat_a1 , cat_a2 , cat_a3 , desaladora , otros , desinf_1 , desinf_2 , desinf_3 , periodicid , organismo , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "POTABILIZACION_ENC_M50", """select '2020' as fase , clave , provincia , municipio , orden_trat , tipo_tra , ubicacion , s_desinf , cat_a1 , cat_a2 , cat_a3 , desaladora , otros , desinf_1 , desinf_2 , desinf_3 , periodicid , organismo , estado
#     from eiel.potabilizacion_enc pe
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_trat , tipo_tra , ubicacion , s_desinf , cat_a1 , cat_a2 , cat_a3 , desaladora , otros , desinf_1 , desinf_2 , desinf_3 , periodicid , organismo , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRAT_POTA_NUCLEO", """select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , po_provin , po_munipi , orden_trat
#     from eiel.trat_pota_nucleo tpn
#     where exists
#     (select 1 from eiel.potabilizacion_enc pe
#     where tpn.fase = pe.fase and tpn.serv_pro = pe.provincia and tpn.serv_mun = pe.municipio and tpn.clave = pe.fase and tpn.orden_trat = pe.orden_trat)""")
#
#         # ----------------------------------------------TRAMO_CARRETERA-----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "tramo_carretera",
#     """select geom , '2020' as "FASE" , provincia "PROV" , cod_carrt "COD_CARRT" , municipio "MUN" , pk_inicial "PK_INICIAL"
#     from eiel.tramo_carretera tc
#     order by fase , provincia , cod_carrt , municipio , pk_inicial""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRAMO_CARRETERA",
#     """select '2020' as fase , provincia , cod_carrt , municipio , pk_inicial , pk_final , titular , gestion , senaliza , firme , estado , ancho , longitud , pasos_nive , dimensiona , muy_sinuos , pte_excesi , fre_estrec
#     from eiel.tramo_carretera tc
#     order by fase , provincia , cod_carrt , municipio , pk_inicial , pk_final , titular , gestion , senaliza , firme , estado , ancho , longitud , pasos_nive , dimensiona , muy_sinuos , pte_excesi , fre_estrec
#     """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CARRETERA", """select distinct '2020' as fase , provincia , cod_carrt , denominaci
#     from eiel.tramo_carretera tc
#     order by fase , provincia , cod_carrt , denominaci""")
#
#         # ---------------------------------------------COLECTOR----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "tramo_colector",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_cole "ORDEN_COLE" , tipo_colec "TIPO_COLEC" , sist_trans "SIST_TRANS" , estado "ESTADO" , titular "TITULAR" , gestion "GESTION"
#     from eiel.tramo_colector tc
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_cole , tipo_colec , sist_trans , estado , titular , gestion""")
#         self.exportar_shape(progressbar, directorio_salida, "tramo_colector_m50",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_cole "ORDEN_COLE" , tipo_colec "TIPO_COLEC" , sist_trans "SIST_TRANS" , estado "ESTADO" , titular "TITULAR" , gestion "GESTION"
#     from eiel.tramo_colector tc
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_cole , tipo_colec , sist_trans , estado , titular , gestion""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "COLECTOR", """select '2020' as fase , clave , provincia , municipio , orden_cole
#     from eiel.tramo_colector tc
#     order by fase , clave , provincia , municipio , orden_cole""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "COLECTOR_ENC", """select '2020' as fase , clave , provincia , municipio , orden_cole
#     from eiel.tramo_colector tc
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_cole""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "COLECTOR_ENC_M50", """select '2020' as fase , clave , provincia , municipio , orden_cole
#     from eiel.tramo_colector tc
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_cole""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRAMO_COLECTOR",
#     """select '2020' as fase , clave , provincia , municipio , orden_cole , tipo_colec , sist_trans , estado , titular , gestion , long_tramo
#     from eiel.tramo_colector tc
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_cole , tipo_colec , sist_trans , estado , titular , gestion , long_tramo""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRAMO_COLECTOR_M50",
#     """select '2020' as fase , clave , provincia , municipio , orden_cole , tipo_colec , sist_trans , estado , titular , gestion , long_tramo
#     from eiel.tramo_colector tc
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_cole , tipo_colec , sist_trans , estado , titular , gestion , long_tramo""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "COLECTOR_NUCLEO",
#     """select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , c_provinci , c_municipi , orden_cole
#     from eiel.colector_nucleo cn
#     where exists
#     (select 1 from eiel.tramo_colector tc
#     where cn.fase = tc.fase and cn.serv_pro = tc.provincia and cn.serv_mun = tc.municipio and cn.clave = tc.clave and cn.orden_cole = tc.orden_cole)""")
#
#         # ---------------------------------------------CONDUCCION----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "tramo_conduccion",
#     """select geom , '2020' as "FASE" , UPPER(clave) "CLAVE" , provincia "PROV" , municipio "MUN" , orden_cond "ORDEN_COND" , tipo_tcond "TIPO_TCOND" , estado "ESTADO" , titular "TITULAR" , gestion "GESTION"
#     from eiel.tramo_conduccion tc
#     where municipio != '275'
#     order by fase , upper(clave) , provincia , municipio , orden_cond , tipo_tcond , estado , titular , gestion""")
#         self.exportar_shape(progressbar, directorio_salida, "tramo_conduccion_m50",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_cond "ORDEN_COND" , tipo_tcond "TIPO_TCOND" , estado "ESTADO" , titular "TITULAR" , gestion "GESTION"
#     from eiel.tramo_conduccion tc
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_cond , tipo_tcond , estado , titular , gestion""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CONDUCCION",
#     """select '2020' as fase , UPPER(clave) , provincia , municipio , orden_cond
#     from eiel.tramo_conduccion tc
#     order by fase , upper(clave) , provincia , municipio , orden_cond""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CONDUCCION_ENC", """select '2020' as fase , UPPER(clave) , provincia , municipio , orden_cond
#     from eiel.tramo_conduccion tc
#     where municipio != '275'
#     order by fase , upper(clave) , provincia , municipio , orden_cond""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "CONDUCCION_ENC_M50", """select '2020' as fase , clave , provincia , municipio , orden_cond
#     from eiel.tramo_conduccion tc
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_cond""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRAMO_CONDUCCION",
#     """select '2020' as fase , UPPER(clave) , provincia , municipio , orden_cond , tipo_tcond , estado , titular , gestion , longitud
#     from eiel.tramo_conduccion tc
#     where municipio != '275'
#     order by fase , upper(clave) , provincia , municipio , orden_cond , tipo_tcond , estado , titular , gestion , longitud""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRAMO_CONDUCCION_M50",
#     """select '2020' as fase , clave , provincia , municipio , orden_cond , tipo_tcond , estado , titular , gestion , longitud
#     from eiel.tramo_conduccion tc
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_cond , tipo_tcond , estado , titular , gestion , longitud""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "COND_AGUA_NUCLEO",
#     """select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , UPPER(clave) , cond_provi , cond_munic , orden_cond
#     from eiel.cond_agua_nucleo can
#     where exists
#     (select 1 from eiel.tramo_conduccion tc
#     where can.fase = tc.fase and can.serv_pro = tc.provincia and can.serv_mun = tc.municipio and can.clave = tc.clave and can.orden_cond = tc.orden_cond)""")
#
#         # ---------------------------------------------TRAMO_EMISARIO----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "tramo_emisario",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_emis "ORDEN_EMIS" , tipo_mat "TIPO_MAT" , estado "ESTADO"
#     from eiel.tramo_emisario te
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_emis , tipo_mat , estado""")
#         self.exportar_shape(progressbar, directorio_salida, "tramo_emisario_m50",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_emis "ORDEN_EMIS" , tipo_mat "TIPO_MAT" , estado "ESTADO"
#     from eiel.tramo_emisario te
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_emis , tipo_mat , estado""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "EMISARIO",
#     """select '2020' as fase , clave , provincia , municipio , orden_emis
#     from eiel.tramo_emisario te
#     order by fase , clave , provincia , municipio , orden_emis""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "EMISARIO_ENC",
#     """select '2020' as fase , clave , provincia , municipio , orden_emis , tipo_vert , zona_vert , distancia
#     from eiel.emisario_enc ee
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_emis , tipo_vert , zona_vert , distancia""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "EMISARIO_ENC_M50",
#     """select '2020' as fase , clave , provincia , municipio , orden_emis , tipo_vert , zona_vert , distancia
#     from eiel.emisario_enc ee
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_emis , tipo_vert , zona_vert , distancia""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRAMO_EMISARIO",
#     """select '2020' as fase , clave , provincia , municipio , orden_emis , tipo_mat , estado , long_terre , long_marit
#     from eiel.tramo_emisario te
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_emis , tipo_mat , estado , long_terre , long_marit""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "TRAMO_EMISARIO_M50",
#     """select '2020' as fase , clave , provincia , municipio , orden_emis , tipo_mat , estado , long_terre , long_marit
#     from eiel.tramo_emisario te
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_emis , tipo_mat , estado , long_terre , long_marit""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "EMISARIO_NUCLEO",
#     """select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , em_provinc , em_municip , orden_emis
#     from eiel.emisario_nucleo en
#     where exists
#     (select 1 from eiel.emisario_enc ee
#     where en.fase = ee.fase and en.serv_pro = ee.provincia and en.serv_mun = ee.municipio and en.clave = ee.clave and en.orden_emis = ee.orden_emis)""")
#
#         # ---------------------------------------------VERTEDERO----------------------------------------------------#
#         self.exportar_shape(progressbar, directorio_salida, "vert_encuestado",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_ver "ORDEN_VER"
#     from eiel.vert_encuestado ve
#     where municipio != '275'
#     order by fase , clave , provincia , municipio , orden_ver""")
#         self.exportar_shape(progressbar, directorio_salida, "vert_encuestado_m50",
#     """select geom , '2020' as "FASE" , clave "CLAVE" , provincia "PROV" , municipio "MUN" , orden_ver "ORDEN_VER"
#     from eiel.vert_encuestado ve
#     where municipio = '275'
#     order by fase , clave , provincia , municipio , orden_ver""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "VERTEDERO",
#     """select '2020' as fase , clave , provincia , municipio , orden_ver
#     from eiel.vert_encuestado ve
#     order by fase , clave , provincia , municipio , orden_ver""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "VERT_ENCUESTADO",
#     """select '2020' as fase , clave , provincia , municipio , orden_ver , tipo_ver , titular , gestion , olores , humos , cont_anima , r_inun , filtracion , impacto_v , frec_averi , saturacion , inestable , otros , capac_tot , capac_porc , capac_ampl , capac_tran , estado , vida_util , categoria , actividad
#     from eiel.vert_encuestado ve
#     where municipio != '275'
#     order by
#     fase , clave , provincia , municipio , orden_ver , tipo_ver , titular , gestion , olores , humos , cont_anima , r_inun , filtracion , impacto_v , frec_averi , saturacion , inestable , otros , capac_tot , capac_porc , capac_ampl , capac_tran , estado , vida_util , categoria , actividad""")
#         self.exportar_txt(self.con, progressbar, directorio_salida, "VERT_ENCUESTADO_M50",
#     """select '2020' as fase , clave , provincia , municipio , orden_ver , tipo_ver , titular , gestion , olores , humos , cont_anima , r_inun , filtracion , impacto_v , frec_averi , saturacion , inestable , otros , capac_tot , capac_porc , capac_ampl , capac_tran , estado , vida_util , categoria , actividad
#     from eiel.vert_encuestado ve
#     where municipio = '275'
#     order by
#     fase , clave , provincia , municipio , orden_ver , tipo_ver , titular , gestion , olores , humos , cont_anima , r_inun , filtracion , impacto_v , frec_averi , saturacion , inestable , otros , capac_tot , capac_porc , capac_ampl , capac_tran , estado , vida_util , categoria , actividad """)
#         self.exportar_txt(self.con, progressbar, directorio_salida, "VERTEDERO_NUCLEO",
#     """select '2020' as fase, serv_pro , serv_mun , serv_ent , serv_nucle , clave , ver_provin , ver_munici , ver_codigo
#     from eiel.vertedero_nucleo vn
#     where exists
#     (select 1 from eiel.vert_encuestado ve
#     where vn.fase = ve.fase and vn.serv_pro = ve.provincia and vn.clave = ve.clave and vn.ver_provin = ve.provincia and
#     vn.ver_munici = ve.municipio and vn.ver_codigo = ve.orden_ver)""")





;VERTEDERO = select '2020' as fase , clave , provincia , municipio , orden_ver
;    from eiel.vert_encuestado ve
;    order by fase , clave , provincia , municipio , orden_ver

;VERTEDERO_NUCLEO = select '2020' as fase, serv_pro , serv_mun , serv_ent , serv_nucle , clave , ver_provin , ver_munici , ver_codigo
;    from eiel.vertedero_nucleo vn
;    where exists
;    (select 1 from eiel.vert_encuestado ve
;    where vn.fase = ve.fase and vn.serv_pro = ve.provincia and vn.clave = ve.clave and vn.ver_provin = ve.provincia and
;    vn.ver_munici = ve.municipio and vn.ver_codigo = ve.orden_ver)


;TRAT_POTA_NUCLEO = select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , po_provin , po_munipi , orden_trat
;    from eiel.trat_pota_nucleo tpn
;    where exists
;    (select 1 from eiel.potabilizacion_enc pe
;    where tpn.fase = pe.fase and tpn.serv_pro = pe.provincia and tpn.serv_mun = pe.municipio and tpn.clave = pe.fase and tpn.orden_trat = pe.orden_trat)


;TRA_POTABILIZACION = select '2020' as fase , clave , provincia , municipio , orden_trat
;    from eiel.potabilizacion_enc pe
;    order by fase , clave , provincia , municipio , orden_trat


;SANEA_AUTONOMO = select '2020' as fase , prov , mun , ent , nucleo , tipo_sanea , estado , adecuacion , sau_vivien , sau_pob_re , sau_pob_es , sau_pob_vi_def , sau_pob_re_def , sau_pob_es_def
;    from eiel.sanea_autonomo sa
;    order by fase , prov , mun , ent , nucleo , tipo_sanea , estado , adecuacion , sau_vivien , sau_pob_re , sau_pob_es , sau_pob_vi_def , sau_pob_re_def , sau_pob_es_def


;RECOGIDAS_BASURAS = select '2020' as fase , provincia , municipio , entidad , nucleo , tipo_rbas , gestion , periodicid , calidad , produ_basu , contenedor
;    from eiel.recogida_basura rb
;    order by fase , provincia , municipio , entidad , nucleo , tipo_rbas , gestion , periodicid , calidad , produ_basu , contenedor


;nucl_encuestado_1 = select '2020' as fase , provincia , municipio , entidad , nucleo , padron , pob_estaci , altitud , viv_total , hoteles , casas_rura , accesib
;    from eiel.nucl_encuestado_1 ne
;    order by fase , provincia , municipio , entidad , nucleo , padron , pob_estaci , altitud , viv_total , hoteles , casas_rura , accesib
;
;nucl_encuestado_2 = select '2020' as fase , provincia , municipio , entidad , nucleo , aag_caudal , aag_restri , aag_contad , aag_tasa , aag_instal , aag_hidran , replace(aag_est_hi, '99', '') , aag_valvul , aag_est_va , aag_bocasr , aag_est_bo , cisterna
;    from eiel.nucl_encuestado_2 ne
;    order by fase , provincia , municipio , entidad , nucleo , aag_caudal , aag_restri , aag_contad , aag_tasa , aag_instal , aag_hidran , aag_est_hi , aag_valvul , aag_est_va , aag_bocasr , aag_est_bo , cisterna
;
;nucl_encuestado_3 = select '2020' as fase , provincia , municipio , entidad , nucleo , aag_v_cone , aag_v_ncon , aag_c_invi , aag_c_vera , aag_v_expr , aag_v_depr , aag_perdid , aag_calida , aag_l_defi , aag_v_defi , aag_pr_def , aag_pe_def
;    from eiel.nucl_encuestado_3 ne
;    order by fase , provincia , municipio , entidad , nucleo , aag_v_cone , aag_v_ncon , aag_c_invi , aag_c_vera , aag_v_expr , aag_v_depr , aag_perdid , aag_calida , aag_l_defi , aag_v_defi , aag_pr_def , aag_pe_def
;
;nucl_encuestado_4 = select '2020' as fase , provincia , municipio , entidad , nucleo , aau_vivien , aau_pob_re , aau_pob_es , aau_def_vi , aau_def_re , aau_def_es , aau_fecont , aau_fencon , aau_caudal
;    from eiel.nucl_encuestado_4 ne
;    order by fase , provincia , municipio , entidad , nucleo , aau_vivien , aau_pob_re , aau_pob_es , aau_def_vi , aau_def_re , aau_def_es , aau_fecont , aau_fencon , aau_caudal
;
;nucl_encuestado_5 = select '2020' as fase , provincia , municipio , entidad , nucleo , syd_pozos , syd_sumide , syd_ali_co , syd_ali_si , syd_calida , syd_v_cone , syd_v_ncon , syd_l_defi , syd_v_defi , syd_pr_def , syd_pe_def , syd_c_desa , syd_c_trat , syd_re_urb , syd_re_rus , syd_re_ind
;    from eiel.nucl_encuestado_5 ne
;    order by fase , provincia , municipio , entidad , nucleo , syd_pozos , syd_sumide , syd_ali_co , syd_ali_si , syd_calida , syd_v_cone , syd_v_ncon , syd_l_defi , syd_v_defi , syd_pr_def , syd_pe_def , syd_c_desa , syd_c_trat , syd_re_urb , syd_re_rus , syd_re_ind
;
;nucl_encuestado_6 = select '2020' as fase , provincia , municipio , entidad , nucleo , rba_v_sser , rba_pr_sse , rba_pe_sse , rba_serlim , rba_plalim
;    from eiel.nucl_encuestado_6 ne
;    order by fase , provincia , municipio , entidad , nucleo , rba_v_sser , rba_pr_sse , rba_pe_sse , rba_serlim , rba_plalim
;
;nucl_encuestado_7 = select '2020' as fase , provincia , municipio , entidad , nucleo , tv_ant , tv_ca , tm_gsm , tm_umts , tm_gprs , correo , ba_rd , ba_xd , ba_wi , ba_ca , ba_rb , ba_st , capi , electricid , gas , alu_v_sin , alu_l_sin
;    from eiel.nucl_encuestado_7 ne
;    order by fase , provincia , municipio , entidad , nucleo , tv_ant , tv_ca , tm_gsm , tm_umts , tm_gprs , correo , ba_rd , ba_xd , ba_wi , ba_ca , ba_rb , ba_st , capi , electricid , gas , alu_v_sin , alu_l_sin
;
;ot_serv_municipal = select '2020' as fase , provincia , municipio , sw_inf_grl , sw_inf_tur , sw_gb_elec , ord_soterr , en_eolica , kw_eolica , en_solar , kw_solar , pl_mareo , kw_mareo , ot_energ , kw_energ , cob_serv_t , tv_dig_cab
;    from eiel.ot_serv_municipal osm
;    order by fase , provincia , municipio , sw_inf_grl , sw_inf_tur , sw_gb_elec , ord_soterr , en_eolica , kw_eolica , en_solar , kw_solar , pl_mareo , kw_mareo , ot_energ , kw_energ , cob_serv_t , tv_dig_cab
;

;inst_depor_deporte = select '2020' as fase, clave, provincia, municipio, entidad, poblamient, orden_inst , tipo_depor
;    from eiel.inst_depor_deporte idd
;    where exists
;    (select 1 from eiel.instal_deportiva id
;    where idd.fase = id.fase and idd.clave = id.clave and idd.provincia = id.provincia and idd.municipio = id.municipio and
;    idd.entidad = id.entidad and idd.poblamient = id.poblamient and idd.orden_inst = id.orden_inst)


;EMISARIO = select '2020' as fase , clave , provincia , municipio , orden_emis
;    from eiel.tramo_emisario te
;    order by fase , clave , provincia , municipio , orden_emis
;
;EMISARIO_ENC = select '2020' as fase , clave , provincia , municipio , orden_emis , tipo_vert , zona_vert , distancia
;    from eiel.emisario_enc ee
;    where municipio != '275'
;    order by fase , clave , provincia , municipio , orden_emis , tipo_vert , zona_vert , distancia
;
;EMISARIO_ENC_M50 = select '2020' as fase , clave , provincia , municipio , orden_emis
;    from eiel.emisario_enc ee
;    where municipio = '275'
;    order by fase , clave , provincia , municipio , orden_emis
;
;EMISARIO_NUCLEO = select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , em_provinc , em_municip , orden_emis
;    from eiel.emisario_nucleo en
;    where exists
;    (select 1 from eiel.emisario_enc ee
;    where en.fase = ee.fase and en.serv_pro = ee.provincia and en.serv_mun = ee.municipio and en.clave = ee.clave and en.orden_emis = ee.orden_emis)


;depuradora = select '2020' as fase, clave , provincia , municipio , orden_depu
;    from eiel.depuradora_enc de
;    order by fase, clave , provincia , municipio , orden_depu""")


;COLECTOR = select '2020' as fase , clave , provincia , municipio , orden_cole
;    from eiel.tramo_colector tc
;    order by fase , clave , provincia , municipio , orden_cole
;
;COLECTOR_ENC = select '2020' as fase , clave , provincia , municipio , orden_cole
;    from eiel.tramo_colector tc
;    where municipio != '275'
;    order by fase , clave , provincia , municipio , orden_cole
;
;COLECTOR_ENC_M50 = select '2020' as fase , clave , provincia , municipio , orden_cole
;    from eiel.tramo_colector tc
;    where municipio = '275'
;    order by fase , clave , provincia , municipio , orden_cole
;
;COLECTOR_NUCLEO = select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , c_provinci , c_municipi , orden_cole
;    from eiel.colector_nucleo cn
;    where exists
;    (select 1 from eiel.tramo_colector tc
;    where cn.fase = tc.fase and cn.serv_pro = tc.provincia and cn.serv_mun = tc.municipio and cn.clave = tc.clave and cn.orden_cole = tc.orden_cole)
;
;COND_AGUA_NUCLEO = select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , UPPER(clave) , cond_provi , cond_munic , orden_cond
;    from eiel.cond_agua_nucleo can
;    where exists
;    (select 1 from eiel.tramo_conduccion tc
;    where can.fase = tc.fase and can.serv_pro = tc.provincia and can.serv_mun = tc.municipio and can.clave = tc.clave and can.orden_cond = tc.orden_cond)
;
;CONDUCCION = select '2020' as fase , UPPER(clave) , provincia , municipio , orden_cond
;    from eiel.tramo_conduccion tc
;    order by fase , upper(clave) , provincia , municipio , orden_cond
;
;CONDUCCION_ENC = select '2020' as fase , UPPER(clave) , provincia , municipio , orden_cond
;    from eiel.tramo_conduccion tc
;    where municipio != '275'
;    order by fase , upper(clave) , provincia , municipio , orden_cond
;
;CONDUCCION_ENC_M50 = select '2020' as fase , UPPER(clave) , provincia , municipio , orden_cond
;    from eiel.tramo_conduccion tc
;    where municipio = '275'
;    order by fase , upper(clave) , provincia , municipio , orden_cond
;
;dep_agua_nucleo = select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , de_provinc , de_municip , orden_depu
;    from eiel.depuradora_agua_nucleo dan
;    where exists
;    (select 1 from eiel.depuradora_enc de
;    where dan.fase = de.fase and dan.serv_pro = de.provincia and dan.serv_mun = de.municipio and dan.clave = de.clave and dan.orden_depu = de.orden_depu)
;
;DEPOSITO = select '2020' as fase , clave , provincia , municipio , orden_depo
;    from eiel.deposito_enc de
;    order by fase, clave, provincia, municipio, orden_depo
;
;DEPOSITO_AGUA_NUCLEO = select '2020' as fase , serv_pro , serv_mun , serv_ent , serv_nucle , clave , de_provinc , de_municip , orden_depo
;    from eiel.deposito_agua_nucleo dan
;    where exists
;    (select 1 from eiel.deposito_enc de
;    where dan.fase = de.fase and dan.serv_pro = de.provincia and dan.serv_mun = de.municipio and dan.clave = de.clave and dan.orden_depo = de.orden_depo)


;CENT_CULTURAL_USOS = select '2020' as fase, clave, provincia, municipio, entidad, poblamient, orden_cent, uso, s_cubi
;    from eiel.cent_cultural_usos ccu
;    where exists
;    (select 1 from eiel.cent_cultural cc2
;    where ccu.fase = cc2.fase and ccu.clave = cc2.clave and ccu.provincia = cc2.provincia and ccu.municipio = cc2.municipio and
;    ccu.entidad = cc2.entidad and ccu.poblamient = cc2.poblamient and ccu.orden_cent = cc2.orden_cent)


;CASA_CON_USO = select '2020' as fase, clave, provincia, municipio, entidad, poblamient, orden_casa, uso, s_cubi
;    from eiel.casa_con_uso ccu
;    where exists
;    (select 1 from eiel.casa_consistorial cc
;    where cc.fase = ccu.fase and cc.clave = ccu.clave and cc.provincia = ccu.provincia and cc.municipio = ccu.municipio and
;    cc.entidad = ccu.entidad and cc.poblamient = ccu.poblamient and cc.orden_casa = ccu.orden_casa)


;CAP_AGUA_NUCLEO = select
;    '2020' as fase, serv_pro, serv_mun , serv_ent , serv_nucle , clave , c_provinc , c_municip , orden_capt
;    from eiel.cap_agua_nucleo can
;    where exists
;    (select 1 from eiel.captacion_enc ce
;    where can.fase = ce.fase and can.serv_mun = ce.municipio and can.clave = ce.clave and can.c_provinc = ce.provincia and can.orden_capt = ce.orden_capt)

;CAPTACION_AGUA = select '2020' as fase , clave , provincia , municipio , orden_capt
;    from eiel.captacion_enc ce
;    order by fase, clave, provincia, municipio , orden_capt
