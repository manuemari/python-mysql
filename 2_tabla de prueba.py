import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="mydatabase" #base creada en la parte 1, todo lo que se haga con el conector sera enfocada en esta base
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE clientes (name VARCHAR (255), address VARCHAR (255))") #creación de la tabla

mycursor.execute("SHOW TABLES")

for x in mycursor: #consulta tablas
    print(x)
