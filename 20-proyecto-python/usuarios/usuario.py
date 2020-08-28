# import mysql.connector
import sqlite3
import datetime

env = 'office'
if env == 'office':
	#Conexion SQLite
	database = sqlite3.connect('sq_master_python')
	cursor =  database.cursor()
	with open('./sqlite_tables.sql') as sqlite_file:
		sql_script = sqlite_file.read()
	cursor.executescript(sql_script)
	# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") #Lista las tablas
	# print(cursor.fetchall())
else:
	#Conexion MySQL
	database = mysql.connector.connect(
		host = 'localhost',
		user = 'emarcelloni',
		password = '3marc3110n1',
		database = 'master_python',
	)
	cursor = database.cursor(buffered = True)

class Usuario:

	def __init__(self,nombre,apellidos,email,password):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.password = password

	def registrar(self):
		fecha = datetime.datetime.now()
		query = "INSERT INTO USUARIOS (nombre,apellidos,email,password,fecha) VALUES(?,?,?,?,?)"
		usuario = (self.nombre,self.apellidos,self.email,self.password,fecha) #Tupla que representa un nuevo usuario.
		cursor.execute(query,usuario)
		database.commit()
		cursor.close()
		return [cursor.rowcount,self] #Retorna en una lista la cantidad de filas afectadas y el objeto mismo.

	def identificar(self):
		return self.nombre
