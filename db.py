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
  string = "SELECT %s FROM %s %s;" %(values,table,conditions)
  cur.execute(string)
  rows = cur.fetchall()
  for row in rows:
    print(row)

def insertIntoDB(table,attributes,values):
    string = "INSERT INTO %s (%s) VALUES (%s);" %(table,attributes,values)
    cur.execute(string)
    get_query = "SELECT %s FROM %s;" %(attributes, table)
    cur.execute(get_query)
    rows = cur.fetchall()
    conn.commit()
    for row in rows:
      print(row)
    

def deleteFromDB(table, conditions):
  query = "DELETE FROM %s %s;" %(table, conditions)
  cur.execute(query)
  get_query = "SELECT * FROM %s %s;" %(table, conditions)
  cur.execute(get_query)
  rows = cur.fetchall()
  conn.commit()
  for row in rows:
    print(row)

def updateFromDB(table, new, conditions):
  update_query = "UPDATE %s SET %s %s;" %(table, new, conditions)
  cur.execute(update_query)
  get_query = "SELECT * FROM %s %s;" %(table, conditions)
  cur.execute(get_query)
  rows = cur.fetchall()
  conn.commit()
  for row in rows:
    print(row)
    
def createTable(name,attributes):
  string = "CREATE TABLE %s( %s);" %(name,attributes)
  cur.execute(string)
  print('CREATED \n')
  conn.commit()

def deleteTable(name):
  string = "DROP TABLE %s;" %(name)
  cur.execute(string)
  print('DELETED \n')
  conn.commit()

cur = conn.cursor()

#Function calls
selectFromDB('*','users','')
insertIntoDB('sequences', "sequence_id, description, completion_count, difficulty, subject, course_type", "8, 'This is a sequence.', 1, 'Easy', 'Computer Science', 'Mixed'")
deleteFromDB('users', 'WHERE user_id=\'1\'')
udpdateFromDB('users', 'email=\'definitelyarealemail@email.com\'', 'WHERE user_id=\'1\'')

cur.close()
conn.close()

