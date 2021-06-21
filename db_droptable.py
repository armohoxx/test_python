import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="0897495923a",
  database="mytestdatabase"
)

mycursor = mydb.cursor()

#Delete the table "customers"
"""
sql = "DROP TABLE customers"

mycursor.execute(sql)
"""

#Delete the table "customers" if it exists
"""
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
"""
