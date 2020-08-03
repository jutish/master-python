# """
# Capturar errores y manejear errores en codigo suceptible a fallos
# """
# try:
# 	nombre = input("Cual es tu nombre?: ")
# 	if len(nombre) > 1:
# 		nombre_usuario = f"El nombre es: {nombre}"
# 	print(nombre_usuario)
# except:
# 	print("Ha ocurrido un error. ")
# else:
# 	print("Todo ha funcionado bien")
# finally:
# 	print("Fin del bloque, esto se ejecuta siempre")		


# lista = [1,2,5,8,15,25]
# busqueda = 5
# try:
# 	res = lista.index(busqueda)
# 	print(f"El numero {busqueda} se encuentra en la pos: {res}")
# except:
# 	print(f"El numero {busqueda} no esta en la lista")	

# #Manejo de multiples excepciones
# try:
# 	numero = input("Nro para elevar al cuadrado: ")
# 	print(f"El cuadrado de {numero} es: {numero**2}")
# except TypeError:
# 	print("Debes convertir tus cadenas a entero")
# except ValueError:
# 	print("Introduce un numero correcto")
# except Exception as e: #Sino entra en ninguno de los anteriores entra aca y puedo ver el error con e.
# 	print("Ha ocurrido un error: ",type(e).__name__)

#Lanzar excepciones
try:
	edad = int(input("Ingresar Edad: "))
	nombre = input("Ingresar Nombre: ")	
	if edad <0 or edad > 100:
		raise ValueError("La edad ingresada no es real")
	elif len(nombre) <= 2:
		raise ValueError("El nombre ingresado no es real")
	else:
		print("Bienvenido al curso de python")
except ValueError as e:
	print("Se produjo un ValueError: ",e)
