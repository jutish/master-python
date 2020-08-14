#ejemplo1
print("#### Ejemplo 1 #######")
color = "Rojo"
if color == "Rojo":
	print("Muy bien gato mi color favorito es Rojo")
else:
	print("Naaa proba de vuelta")

print("\n#### Ejemplo 2 #####")
# year = input("En que año estamos? ")
year= 2020
if int(year) >= 2021:
	print("El año es mayor o igual a 2021")
else:
	print("El año es menor a 2021")

print("\n#### Ejemplo 3 #####")
nombre = "Esteban"
edad = 18
mayoria = 18
continente = "America"
ciudad = "General Deheza"
if edad >= mayoria:
	print(f"{nombre} es mayor de edad")
	if continente != "Europa":
		print(f"El usuario no es Europeo! es de {ciudad}, {continente}")
	else:
		print("El usuario es Europeo")
else:
	print(f"{nombre} no es mayor de edad")

print("\n#### Ejemplo 4 #####")
# dia = int(input("Ingrese el dia de la semana: "))
dia = 5
if dia == 1:
	print("Es lunes")
elif dia == 2:
	print("Es martes")
elif dia == 3:
	print("Es miercoles")
elif dia == 4:
	print("Es jueves")
elif dia == 5:
	print("Es viernes")
else:
	print("Es fin de semana")

print("\n#### Ejemplo 5 #####")
edad = 25
edad1 = 18
edad2 = 65

if edad >= edad1 and edad <=65:
	print("Esta en edad de trabajar")
else:
	print("No puede trabajar")	

print("\n#### Ejemplo 6 #####")
pais = "Alemania"

if pais == "Argentina" or pais == "España" or pais == "Mexico":
	print(f"El pais {pais} es de habla hispana")
else:
	print(f"{pais} no es de habla hispana")

print("\n#### Ejemplo 7 #####")
pais = "Argentina"

if not (pais == "Argentina" or pais == "España" or pais == "Mexico"):
	print(f"El pais {pais} NO es de habla hispana")
else:
	print(f"{pais} SI es de habla hispana")

	print("\n#### Ejemplo 8 #####")

pais = "Mexico"
if pais != "Argentina" or pais != "España" or pais != "Mexico":
	print(f"El pais {pais} NO es de habla hispana")
else:
	print(f"{pais} SI es de habla hispana")