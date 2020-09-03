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

	def mostrar(self,usr):
		print(f"\nVale usuario {usr[1]} aquí tienes tus notas!!!")
		nota = modelo.Nota(usr[0],'','')
		notas = nota.listar()
		for nt in notas:
			print(f"\n**************Nota {notas.index(nt)}*******************")
			print(f"Titulo: {nt[2]}")
			print(f"Contenido: {nt[3]}")
			print("****************************************")

	def borrar(self,usr):
		print(f"Hola {usr[1]} vamos a borrar notas!!")
		titulo = input("Ingresa el titulo de la nota que deseas borrar: ")
		try:
			nota = modelo.Nota(usr[0],'','')
			borrar = nota.borrar(titulo)
			if borrar[0]>=1:
				print(f"Perfecto has borrado la nota {titulo}")
			else:
				print(f"No se ha encontrado la nota {titulo}! No se pudo borrar")	
		except Exception as e:
			print(f"No se ha logrado borrar la nota {titulo}")
			print("Ha ocurrido un error: ",type(e).__name__)