import mysql.connector
config = {
  'user': 'root',
  'password': '123456',
  'host': '127.0.0.1',
  'database': 'WTFDB',
  'raise_on_warnings': True
}
conn = None
def initConnection():
    conn = mysql.connector.connect(**config)
    return conn
def closeConnection():
    conn.close()