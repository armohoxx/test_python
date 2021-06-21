import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="0897495923a",
  database="mytestdatabase"
)

mycursor = mydb.cursor()

#Select record(s) where the address is "Thailand"
"""
sql = "SELECT * FROM customers WHERE address ='Thailand'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""

#Select records where the address contains the word "way"
"""
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""

#Escape query values by using the placholder %s method
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

