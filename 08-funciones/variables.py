"""
Variables globales y locales
"""

frase = "Nadie es tan lindo como la foto de Instagram ni tan feo como la del DNI"
def getFrase():
	frase = "A la grande le puse cuca"
	print("Local: " + frase)


print("Global: " + frase)
getFrase()

#Puedo tomar una variable local y hacerla global despues de ejecutar la funcion.
#Se usa la palabra reservada global y el nombre de la variable.

def getLocal():
	global local
	local = "Esta es un var. Local, pero se puede acceder desde afuera"
	print(local)

getLocal()
print(local)