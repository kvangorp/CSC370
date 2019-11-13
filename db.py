import sys, csv, psycopg2
# Open db connection here

psql_user = 'daytondep'
psql_db = 'delphi'
psql_password = 'V00882488'
psql_server = 'studentdb1.csc.uvic.ca'
psql_port = 5432
conn = psycopg2.connect(dbname=psql_db,
    user=psql_user,
    password=psql_password,
    host=psql_server,
    port=psql_port) 


#Sample query
#cur = conn.cursor()
#cur.execute("select max(prcp), city from test_rain group by city;")
#rows = curr.fetchall()
#for row in rows:
#    print(row)

