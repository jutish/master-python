# import mysql.connector
import sqlite3
import datetime
import hashlib
import usuarios.conexion as conexion

class Usuario:

	def __init__(self,nombre,apellidos,email,password):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.password = password
		#Me conecto a la BD cada vez que creo un objeto Usuario.
		self.conectar = conexion.conectar()
		self.database = self.conectar[0] 
		self.cursor = self.conectar[1]

	def registrar(self):
		fecha = datetime.datetime.now()
		passCifrado = hashlib.sha256(self.password.encode('utf8')).hexdigest()
		query = "INSERT INTO USUARIOS (nombre,apellidos,email,password,fecha) VALUES(?,?,?,?,?)"
		usuario = (self.nombre,self.apellidos,self.email,passCifrado,fecha) #Tupla que representa un nuevo usuario.
		try:
			self.cursor.execute(query,usuario)
			self.database.commit()
			result = [self.cursor.rowcount,self]
		except:
			result = [0,self]

		return result
			
	def identificar(self):
		passCifrado = hashlib.sha256(self.password.encode('utf8')).hexdigest()
		query = "SELECT * FROM USUARIOS WHERE email = ? AND password = ?"
		identificador = (self.email,passCifrado)
		self.cursor.execute(query,identificador)
		res = self.cursor.fetchone() #Devuelve una tupla
		return res

