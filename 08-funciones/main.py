# """
# Definicion de funciones.
# def miFuncion(parametros):
# 	defino mi funcion
# """
# print("#####Ejemplo 1######")
# def muestraNombre():
# 	print("Victor")
# 	print("Paco")
# 	print("Micho")
# 	print("Tito")
# 	print("Cabezon")
# 	print("\n")
# muestraNombre()
# muestraNombre()

# """
# Parametros en funciones.

# """
# print("#####Ejemplo 2######")
# def mostrarTuNombre(nombre,edad):
# 	print(f"Tu nombre es: {nombre}")
# 	if edad >= 18:
# 		print("Eres mayor de edad")

# nombre = input("Introduce tu nombre: ")
# edad = int(input("Introduce tu edad: "))
# mostrarTuNombre(nombre,edad)

# print("\n#####Ejemplo 3######")

# def tabla(nro):
# 	print(f"Tabla del {nro}")
# 	for i in range(1,11):
# 		print(f"{nro} x {i} = {nro * i}")

# nro = int(input("La tabla de que numero desea conocer? "))
# tabla(nro)


"""
Parametros opcionales
Se le pone un valor por defecto, entonces lo hago opcional de esa forma.
"""
# print("\n#####Ejemplo 4######")

# def getEmpleado(nombre,dni=None):
# 	print("Empleado")
# 	print(f"{nombre}")
# 	if dni!=None:
# 		print(f"{dni}")


# getEmpleado("Esteban",32585911)

"""
Parametros opcionales y Return"
"""
print("\n#####Ejemplo 5######")

def saludame(nombre):
	sal = f"Hola {nombre} como has estado?"
	return sal

print(saludame("Esteban"))

print("\n#####Ejemplo 6######")
#Si basicas es igual a True (cualquier numero distinto de 0 funciona tambien) entonces solo muestra las basicas. 
#Sino muestra todas
def calculadora(nro1,nro2,basicas = False):
	suma = nro1 + nro2
	resta = nro1 - nro2
	multi = nro1 * nro2
	div = nro1 / nro2

	cadena = ""
	cadena += f"Suma: {suma} \n"
	cadena += f"Resta: {resta} \n"
	if basicas == False:
		cadena += f"Multiplicacion: {multi} \n"
		cadena += f"Division: {div} \n"

	return cadena

print(calculadora(5,2,False))

"""
Usar funciones dentro de otras funciones
"""
print("\n#####Ejemplo 7######")

def getNombre(nombre):
	nombre = f"El nombre es: {nombre} "
	return nombre

def getApellido(apellido):
	apellido = f"el apellido es: {apellido} "
	return apellido 

def getTodo(nombre, apellido):
	todo = f"{getNombre(nombre)} y {getApellido(apellido)}"
	return todo

print(getTodo("Esteban","Marcelloni"))

"""
Funciones lambda. Es una funcion anonima, es decir sin nombre.
Sirven para tareas simples
"""
print("\n#####Ejemplo 8######")

getYear = lambda year: f"El año es:{year}"
print(getYear(2021))
	