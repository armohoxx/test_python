import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="0897495923a",
  database = "mytestdatabase"
)

cursor = db.cursor()

#insert one row
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("armyxx", "Thailand")
cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record inserted.")
"""

#insert multiple rows
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

cursor.executemany(sql, val)

db.commit()

print(cursor.rowcount, "was inserted.")

#Get Inserted ID
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
cursor.execute(sql, val)

db.commit()

print("1 record inserted, ID:", cursor.lastrowid)
"""