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

cursor = database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute("SHOW DATABASES") #Dentro de cursor, tengo todas las bases de datos.

for db in cursor:
	print(db)

#Crear Tablas
cursor.execute("""
	CREATE TABLE IF NOT EXISTS vehiculos(
	id INT(10) auto_increment NOT NULL,
	marca VARCHAR(40) NOT NULL,
	modelo VARCHAR(40) NOT NULL,
	precio FLOAT(10,2) NOT NULL,	
	CONSTRAINT PK_VEHICULO PRIMARY KEY(id)) 
""")

cursor.execute("SHOW TABLES")
for tb in cursor:
	print(f"Tablas: {tb}")

# cursor.execute("INSERT INTO vehiculos VALUES(NULL,'Peugeot','308 Active',450000.50)")
# database.commit()

#Insertar varios vehiculos de una vez
vehiculos = [
	('Peugeot','5008 Allure',1500000.25),
	('Fiat','Bravo',750000.50),
	('Honda','HR-V Full',2500000.75),
	('BMW','X6',6500000.35)
]

cursor.executemany('INSERT INTO vehiculos VALUES(NULL,%s,%s,%s)',vehiculos)
database.commit()

#SELECT
cursor.execute("SELECT * FROM vehiculos")
results = cursor.fetchall()
for rs in results:
	print(f"Marca: {rs[1]} - Modelo: {rs[2]} - Precio: {rs[3]}")

#Saca el primer resultado
cursor.execute("SELECT * FROM vehiculos")
auto = cursor.fetchone()
print(auto)

#Borrar
# cursor.execute("DELETE FROM vehiculos")
# database.commit()
# print("Filas Borradas",cursor.rowcount)

#Actualizar
cursor.execute("UPDATE vehiculos SET modelo =  'X5' WHERE modelo = 'X6'")
print(f"Filas Afectadas: {cursor.rowcount}")
database.commit()

