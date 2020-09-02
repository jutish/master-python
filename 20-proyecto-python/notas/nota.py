import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
	def __init__(self,usr_id,titulo,descripcion):
		self.usr_id = usr_id
		self.titulo = titulo
		self.descripcion = descripcion

	def guardar(self):
		query = "INSERT INTO notas (usr_id,titulo,descripcion) values(?,?,?,?)"
		nota = (self.usr_id,self.titulo,self.descripcion,NOW())
		cursor.execute(query,nota)
		database.commit()
		return [cursor.rowcount,self]