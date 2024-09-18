import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",
    database="mydatabase"
)

mycursor =  mydb.cursor()

sql = "INSERT INTO clientes (name,address) VALUES (%s, %s)" #insertar nuevos valores en la tabla
val=("jhon", "higway 21")

mycursor.execute(sql,val)
mydb.commit() #confirmación de que voy a agragar nueva información a mi data base

print(mycursor.rowcount, "fila(s) ingresada(s)")




