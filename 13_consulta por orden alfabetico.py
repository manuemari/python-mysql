import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="*********",
    database="mydatabase"
)

mycursor =  mydb.cursor()

sql = " SELECT * FROM clientes1 ORDER BY name"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)