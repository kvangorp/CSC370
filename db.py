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

#dont know if this  works or not just writing stuff
#update : works!
def selectFromDB(values,table,conditions):
  cur = conn.cursor()
  string = "SELECT %s FROM %s %s;" %(values,table,conditions)
  cur.execute(string)
  rows = cur.fetchall()
  for row in rows:
    print(row)

def deleteFromDB(table, conditions):
  cur = conn.cursor()
  query = "DELETE FROM %s %s;" %(table, conditions)
  cur.execute(query)
  rows = cur.fetchall()
  for row in rows:
    print(row)

def updateFromDB(table, conditions):
  cur = conn.cursor()
  query = "UPDATE %s SET %s %s;" %(table, set, conditions)
  cur.execute(query)
  rows = cur.fetchall()
  for row in rows:
    print(row)

#Function calls
selectFromDB('*','users','')
deleteFromDB()
updateFromDB()

