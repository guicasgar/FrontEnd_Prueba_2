import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect("host='ortho4' port='5433' dbname='eiel_zamora' user='postgres' password='Seresco_2000' connect_timeout=10")

cur = conn.cursor()
cur.execute("""select max(fecha) from informes.sincronizaciones where usuario = 'cesarag'""")
rows = cur.fetchall()
if len(rows) == 0:
    raise Exception("No se encontró el usuario %s en la tabla 'sincronizaciones' del esquema 'informes'")

fecha_ultima_sincro = rows[0][0]


capa = 'SER_anotaciones'

cur = conn.cursor(cursor_factory=RealDictCursor)
sql = """select ser_uuid, ser_fecha_mod from eiel.\"%s\" where ser_fecha_mod > '%s'""" % (capa, fecha_ultima_sincro)
cur.execute(sql)
eregistros = []
for row in cur.fetchall():
    print(row['ser_uuid'])

cur.close()



cur = conn.cursor()
cur.execute("ROLLBACK")
cur.close()

import psycopg2
conn_local = psycopg2.connect("host='localhost' port='5433' dbname='eiel_zamora' user='postgres' password='Seresco_2000' connect_timeout=10")
conn_remoto = psycopg2.connect("host='eielzamora' port='5432' dbname='eiel_zamora' user='postgres' password='admin@985' connect_timeout=10")

curlocal = conn_local.cursor()
curremoto = conn_local.cursor()
AT TIME ZONE 'Europe/Madrid'
sql = 'select ser_fecha_mod from eiel.infraestr_viaria where ser_uuid::text = \'833e74ee-9a11-462d-8fbe-3395beeb5879\''
curlocal.execute(sql)
print(curlocal.fetchone()[0])

curremoto.execute(sql)
print(curremoto.fetchone()[0])
