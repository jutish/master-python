#Crear variables y asignar un valor
texto = "Master en python"
texto2="Con victor roblez"
numero = 45
decimal = 6.7
print(texto)
print(texto2)
print(numero)
print(decimal)
numero = 7
decimal = 8.9
print("----------------------")
print(numero)
print(decimal)
print("----------------------")
#Concatenacion
nombre = "Esteban Eduardo"
apellidos = "Marcelloni"
web = "emarcelloni.com"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))