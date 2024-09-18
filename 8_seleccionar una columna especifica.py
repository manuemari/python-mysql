import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="**********",
    database="mydatabase"
)

mycursor =  mydb.cursor()

mycursor.execute("SELECT name, address FROM clientes1")

myresult = mycursor.fetchall()

for x in myresult:
    print(x) #muestra los resultados de ls consulta, no tiene en cuenta el id