# import mysql.connector
import sqlite3
import datetime
import hashlib
import usuarios.conexion as conexion

conectar = conexion.conectar()
database = conectar[0] 
cursor = conectar[1]

class Usuario:

	def __init__(self,nombre,apellidos,email,password):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.password = password

	def registrar(self):
		fecha = datetime.datetime.now()
		passCifrado = hashlib.sha256(self.password.encode('utf8')).hexdigest()
		query = "INSERT INTO USUARIOS (nombre,apellidos,email,password,fecha) VALUES(?,?,?,?,?)"
		usuario = (self.nombre,self.apellidos,self.email,passCifrado,fecha) #Tupla que representa un nuevo usuario.
		try:
			cursor.execute(query,usuario)
			database.commit()
			result = [cursor.rowcount,self]
		except:
			result = [0,self]

		return result
			
	def identificar(self):
		passCifrado = hashlib.sha256(self.password.encode('utf8')).hexdigest()
		query = "SELECT * FROM USUARIOS WHERE email = ? AND password = ?"
		identificador = (self.email,passCifrado)
		cursor.execute(query,identificador)
		res = cursor.fetchone() #Devuelve una tupla
		return res

