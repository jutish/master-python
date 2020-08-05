from coche import Coche

carro = Coche("Gris","Peugeot","308 Active",200,140,4)
carro1 = Coche("Gris","Honda","H-RV Active",250,160,5)
carro2 = Coche("Blanco y Rojo","Peugeot","3008",200,140,4)
carro3 = Coche("Azul","BMW","X6",250,200,5)
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())


#Detectar Tipado, comparando con el nombre de la clase que queremos comprobar.
if type(carro3)==Coche:
	print("Es un objeto del tipo Coche")
else:
	print("No es del tipo coche")


#Visibilidad
print(carro.soy_publico)
print(carro.getPrivado())


		