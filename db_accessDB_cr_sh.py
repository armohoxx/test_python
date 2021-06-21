import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="0897495923a",
  database = "mytestdatabase"
)

cursor = db.cursor()

#cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") #สร้างตารางพร้อม primary key

cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #create column with primary key (exit table)

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)
