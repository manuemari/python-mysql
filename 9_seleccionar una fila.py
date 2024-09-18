import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",
    database="mydatabase"
)

mycursor =  mydb.cursor()

mycursor.execute("SELECT * FROM clientes1")

myresult = mycursor.fetchone()
print(myresult) #como solo quiero que me muestre un resultado, no es necesario hacer el for, es sola una consulta