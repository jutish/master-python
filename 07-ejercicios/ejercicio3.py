"""
Imprimir el cuadrado de los primeros 60 numeros naturales
Usando For y While
"""

for i in range(1,60):
	print(f"El cuadrado de {i} es : {i**2}")

cont = 0
print("Usando While")
while cont <= 60:
	print(f"El cuadrado de {cont} es: {cont**2}")
	cont+=1

