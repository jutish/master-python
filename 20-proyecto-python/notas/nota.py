import usuarios.conexion as conexion
import datetime

class Nota:
	def __init__(self,usr_id,titulo,descripcion):
		self.usr_id = usr_id
		self.titulo = titulo
		self.descripcion = descripcion
		#Me conecto cuando creo una nueva nota
		self.connect = conexion.conectar()
		self.database = self.connect[0]
		self.cursor = self.connect[1]



	def guardar(self,titulo):
		fecha = datetime.datetime.now()
		query = "INSERT INTO notas (usr_id,titulo,descripcion,fecha) values(?,?,?,?)"
		nota = (self.usr_id,self.titulo,self.descripcion,fecha)
		self.cursor.execute(query,nota)
		self.database.commit()
		return [self.cursor.rowcount,self]

	def listar(self):
		try:
			query = f"SELECT * FROM notas WHERE usr_id = {self.usr_id}"
			self.cursor.execute(query)
			res = self.cursor.fetchall()
		except Exception as e:
			print("Ha ocurrido un error: ",type(e).__name__)	
			res = None
		return res

	def borrar(self,titulo):
		sql = f"DELETE FROM notas WHERE usr_id = {self.usr_id} AND titulo LIKE '%{titulo}%'"
		self.cursor.execute(sql)
		self.database.commit()
		return [self.cursor.rowcount,self]
