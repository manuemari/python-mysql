import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "*********"
)

#print(mydb) #codigo para conectar con mysql

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase") #recordar el nombre que tiene la base de datos

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
