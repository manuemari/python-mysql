import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",
    database="mydatabase"
)

mycursor =  mydb.cursor()

sql = "SELECT * FROM clientes1 WHERE address = %s"
adr = ("Yellow Garden 2",)

mycursor.execute(sql,adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x) #consutlo información