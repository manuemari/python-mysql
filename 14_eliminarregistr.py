import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="mydatabase"
)

mycursor =  mydb.cursor()

sql = "DELETE FROM clientes1 WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"borrador ")