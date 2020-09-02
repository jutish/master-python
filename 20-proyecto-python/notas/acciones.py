import notas.nota as modelo
class Accion:
	def crear(self,usr):
		print(f"Ok {usr[1]}  vamos a crear una nueva Nota!!")
		titulo = input("\nIntroduce el titulo de tu nota: ")
		descripcion = input("Introduce el contenido de tu nota: ")
		nota = modelo.Nota(usr[0],titulo,descripcion) #Creo el objeto Nota pasandole el Usr_id, el titulo y la descrip.
		guardar = nota.guardar()
		if guardar[0]>=1:
			print(f"Perfecto has guardado la nota {nota.titulo}")
		else:
			print(f"No se ha gardado la nota {usr[1]}")