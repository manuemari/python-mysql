import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="mydatabase"
)

mycursor =  mydb.cursor()

sql = "INSERT INTO clientes1 (name, address) VALUE (%s, %s)"
val = ("Michelle", "Blue village")

mycursor.execute(sql, val)
mydb.commit()

print("1 guardado, ID: ", mycursor.lastrowid)