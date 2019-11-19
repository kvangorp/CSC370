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
  get_query = "SELECT * FROM %s %s;" %(table, conditions)
  cur.execute(get_query)
  rows = cur.fetchall()
  for row in rows:
    print(row)

def updateFromDB(table, new, conditions):
  cur = conn.cursor()
  update_query = "UPDATE %s SET %s %s;" %(table, new, conditions)
  cur.execute(update_query)
  get_query = "SELECT * FROM %s %s;" %(table, conditions)
  cur.execute(get_query)
  rows = cur.fetchall()
  for row in rows:
    print(row)

#Function calls
selectFromDB('*','users','')
deleteFromDB('users', 'WHERE user_id=\'1\'')
updateFromDB('users', 'email=\'definitelyarealemail@email.com\'', 'WHERE user_id=\'1\'')

