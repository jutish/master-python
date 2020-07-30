"""
Hacer un programa con 8 enteros
1-Recorrerla y mostrarla
2-Hacer una funcion que la recorra y la devuelva como String. 
3-Ordenarla y mostrarla
4-Mostrar su longitud
5-Buscar algun elemento que el usuario pida por teclado
"""
lista = [5,8,3,10,20,4,65,35]
#1
for ls in lista:
	print(f"Elemento: {lista.index(ls)} Valor: {ls}")

#2
def toCadena(lista):
	salida = ""
	for ls in lista:
		salida += str(ls)+"\n"
	return salida
print(toCadena(lista))
print(toCadena(["hola","chicos",'nada','de nada']))

#3
lista.sort()
print("\n")
for ls in lista:
	print(f"Elemento: {lista.index(ls)} Valor: {ls}")

#4
print(f"\nLargo de la lista: {len(lista)} ")

#5
vBuscado = -1
while not isinstance(vBuscado,int) or vBuscado < 0:
	indice = int(input("Ingrese el valor buscado: "))
	print(f"El valor {indice} se encuentra en la pos: {lista.index(indice)}") #Los errores lanzados por index lo vemos mas adelante.

	
