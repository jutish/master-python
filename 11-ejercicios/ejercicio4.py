"""
Crear un script que tenga 4 variables una Lista, String, un Entero, una Bool.
Y que imprima un mensaje segun el tipo de dato.
Primero hacerlo normal y luego con funciones.
"""

var1 = []
var2 = "Pepe"
var3 = 15
var4 = True

def check(variable,formato=0):
	if formato == 1:
		print(f"La variable es del tipo: {type(variable)}")
	else:
		if isinstance(variable,type([])): print("Tipo Lista")
		if isinstance(variable,type("")):  print("Tipo String")
		if isinstance(variable,type(15)):  print("Tipo Entero")
		if isinstance(variable,type(True)): print("Tipo Booleano")

check(var1)
check(var2)
check(var3)
check(var4)