resultado = 0
for contador in range(0,5):
	print(f"El contador es: {contador}")
	resultado += contador
print("El resultado es",resultado)

numero_usuario = int(input("De que numero quieres ver la tabla? "))
if numero_usuario < 1:
	numero_usuario = 1

print(f"Tabla del numero {numero_usuario}")

for numero in range(1,11):
	if numero_usuario == 45:
		print("No se puede ingresar el numero 45! Chao")
		break
	
	print(f"{numero_usuario} x {numero} = {numero_usuario*numero}")

else:
	print("Tabla terminada")