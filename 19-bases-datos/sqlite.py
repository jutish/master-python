"""
Sqlite ya viene instalado en el lenguaje python.
Se guarda en un archivo que se graba en el proyecto
"""
import sqlite3

#Conexion
conexion = sqlite3.connect('pruebas.db')

#Crear cursor.
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
	"id INTEGER PRIMARY KEY AUTOINCREMENT,"
	"titulo VARCHAR(255),"+
	"descripcion TEXT," + 
	"precio INT)"
	)

#Crear tabla o cualquier consulta usando multilineas
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos( 
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	titulo VARCHAR(255),
	descripcion TEXT, 
	precio INT);
	""")

#Guardar cambios
conexion.commit()

# # Borrar registros
# cursor.execute("DELETE FROM productos")
# conexion.commit()

#Insertar datos
cursor.execute("INSERT INTO productos VALUES(NULL,'Segundo Producto','descripcion de mi producto',550)")
conexion.commit()

#Insertar varios registros de golpe.
productos = [
	("PC Gamer","Tremenda PC",750),
	("Xiaomi A2","Celular usado",1000),
	("Notebook","Notebook lenovo ac560",10000),
	("Guitarra","Guitarra Criolla cuerdas nylon",4222),
]
cursor.executemany("INSERT INTO productos VALUES(NULL,?,?,?)",productos)
conexion.commit()

cursor.execute("UPDATE productos SET precio = 880 WHERE productos.id = 31")
conexion.commit
#Lectura de datos
cursor.execute("SELECT * FROM productos")

producto = cursor.fetchone() #El cursor avanza si esto lo ejecuto despues del for. No trae nada
print(f"Primer registro: {producto}")	

productos = cursor.fetchall()
for pr in productos:
	print(f"ID: {pr[0]} Nombre: {pr[1]}, Titulo: {pr[2]}, Precio: {pr[3]} \n")


#Cerrar conexion
conexion.close()