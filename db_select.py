import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="0897495923a",
  database="mytestdatabase"
)

mycursor = mydb.cursor()

#Select all records from the "customers"
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall() ### We use the fetchall() method, which fetches all rows from the last executed statement. ###

for x in myresult:
  print(x)

#Select only the name and address columns
"""
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""

#Fetch only one row
"""
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
"""




