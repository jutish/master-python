import usuarios.usuario as modelo 

class Acciones:
	
	def registro(self):
		print('\nVamos a registrarte en el sistema')
		nombre = input('¿Cual es tu nombre?: ')
		apellidos = input('¿Cuales son tus apellidos?: ')
		email = input('Ingresa tu correo electronico: ')
		password = input('Ingresa tu password: ')

		usr = modelo.Usuario(nombre,apellidos,email,password) #Creo un nuevo usuario.
		reg = usr.registrar() #guardo lo devuelto

		if reg[0]>=1:
			print(f"Perfecto {reg[1].nombre} te has registrado con el email: {reg[1].email}")
		else:
			print("No te has registrado correctamente")

	def login(self):
		print('\nIdentificate en el sistema')
		email = input('Ingresa tu no correo electronico: ')
		password = input('Ingresa tu password: ')
		try:
			usr = modelo.Usuario('','',email,password)
			login = usr.identificar()
			if email == login[3]: #login[3] contiene el correo leido desde Base de Datos
				print(f"\nBienvenido {login[1]} {login[2]}")
				self.proximasAcciones(login)

		except Exception as e:
			print("Ha ocurrido un error: ",type(e).__name__)
			print("Login incorrecto! Intenta mas tarde")
				
	def proximasAcciones(self,login):
		print("""
		Acciones Disponibles:
		- Crear nota (crear)
		- Mostrar notas (mostrar)
		- Eliminar nota (eliminar)
		- Salir (salir)	
		""")

		accion = input('¿Que quieres hacer?: ')

		if accion == 'crear':
			print("Crear")
		elif accion == 'mostrar':
			print("Mostrar")
		elif accion == 'eliminar':
			print("Eliminar")
		elif accion =='salir':
			print("Salir")
			exit()
		else:
			print("Accion desconocida")		

