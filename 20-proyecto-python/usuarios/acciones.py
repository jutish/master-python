import usuarios.usuario as modelo 
import notas.acciones as acciones

class Acciones:
	def __init__(self):
		self.intentos = 3

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
			#print("Ha ocurrido un error: ",type(e).__name__)
			self.intentos -= 1
			print(f"Login incorrecto! Tienes {self.intentos} intentos restantes")
			if self.intentos > 0:
				self.login()
			else:
				exit()	

	def proximasAcciones(self,login):
		print("""
		Acciones Disponibles:
		- Crear nota (crear)
		- Mostrar notas (mostrar)
		- Eliminar nota (eliminar)
		- Salir (salir)	
		""")

		hazEl = acciones.Accion()
		accion = input('¿Que quieres hacer?: ')
		
		if accion == 'crear':
			hazEl.crear(login)
			self.proximasAcciones(login)
		elif accion == 'mostrar':
			hazEl.mostrar(login)
			self.proximasAcciones(login)
		elif accion == 'eliminar':
			hazEl.borrar(login)
			self.proximasAcciones(login)
		elif accion =='salir':
			print("Salir")
			print(f"Ok {login[1]} Nos vemos!!")
			exit()
		else:
			print("Accion desconocida")		

