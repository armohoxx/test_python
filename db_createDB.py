import mysql.connector
from mysql.connector.errors import custom_error_exception

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="0897495923a"
)

cursor = db.cursor()

cursor.execute(("CREATE DATABASE mytestdatabase"))