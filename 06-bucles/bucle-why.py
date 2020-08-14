contador = 0
while contador < 100:
	print(f"Estoy en {contador}")
	contador += 1

valor = int(input("Que tabla quiere ver? "))

cont = 1 
while cont <= 10:
	print(f"{valor} x {cont} = {valor * cont}")
	cont += 1
else:
	print("Tabla terminada")
