import mysql.connector

#Creamos conexion con la BD
database = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='3marc3110n1',
	database='master_python'
)

#Como saber si la conexion es correcta?
# print(database) 

cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute("SHOW DATABASES") #Dentro de cursor, tengo todas las bases de datos.

for db in cursor:
	print(db)