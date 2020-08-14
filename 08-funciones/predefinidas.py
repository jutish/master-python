nombre = "Esteban Marcelloni"

print(nombre)
print(type(nombre))

#detectar tipado - str, float,....
comprobar = isinstance(nombre,str)
if comprobar:
	print("Esa variable es un String")
else:
	print("no es una cadena")

#limpiar espacios
frase = "   hola carola    "
print(frase)
print(frase.strip())

#Eliminar variables
year = 2020
print(year)
del year #borra la variable

#Comprobar variables vacias
text = "  ff  "
if len(text) <= 0:
	print("La variable esta vacia.")
else:
	print("La variable tiene contenido ", len(text))

#Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar
frase = "La vida es bella"
print(frase.replace("vida","cerveza"))

#Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())