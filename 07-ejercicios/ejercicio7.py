"""
Mostrar los nros. impares, entre dos nros. elegidos
por el usuario
"""
n1 = int(input("Ingrese 1er nro: "))
n2 = int(input("Ingrese 2do nro: "))
print(f"Los nros. impares entre {n1} y {n2} son: ")
for i in range(n1,n2+1):
	if i%2 != 0:
		print(i)