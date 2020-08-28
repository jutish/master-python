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