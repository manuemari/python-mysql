import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="mydatabase"
)

mycursor =  mydb.cursor()

sql = "SELECT * FROM clientes1 WHERE address like '%way%'" #solo me interesa que tenga las letras way, no importa la posición

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult: 
    print(x)


