import mysql.connector #rescatar toda la información que se tenga en el data base

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="mydatabase"
)

mycursor =  mydb.cursor()

mycursor.execute("SELECT * FROM clientes1")

myresult = mycursor.fetchall()

for x in myresult: #llama todos los datos de la consulta sql
    print(x)

