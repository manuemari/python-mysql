import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="********+",
    database="mydatabase"
)

mycursor =  mydb.cursor()

sql = "SELECT * FROM clientes1 WHERE address = 'Sky st 331'"

mycursor.execute(sql)
myresult = mycursor.fetchall() #fetchall pq necesito que revise a todas las posibles personas que se enucentran en ese database

for x in myresult:
    print(x) #consulta de x cliente que viva en la dirreción del statement
