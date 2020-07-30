"""
Escribir un programa que añada valores a una lista mientras
que su longitud sea menor a 120 y mostrarlo por pantalla
"""

lista = []
while  len(lista)<120:
	lista.append(len(lista)+1)
print(lista)
print(len(lista))

lista = []
for ls in range(0,120):
	lista.append(ls)
print(lista)
print(len(lista))