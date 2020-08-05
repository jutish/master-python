#Programacion orientada a objetos

#Definir una clase
class Coche:
	#Atributos
	color = "Rojo"
	marca = "Ferrari"
	modelo = "Aventador"
	velocidad = 300
	caballaje = 500
	plazas = 2
	#Metodos
	def acelerar(self):
		self.velocidad += 1

	def frenar(self):
		self.velocidad -= 1

	def getVelocidad(self):
		return self.velocidad	

	def setColor(self,color):
		self.color = color

	def getColor(self):
		return self.color

	def setModelo(self,modelo):
		self.modelo = modelo

	def getModelo(self):
		return self.modelo	
		
print("########Coche1#########")
coche = Coche() #Creo un objeto. Instancio el coche.
print(f"Velocidad Actual {coche.getVelocidad()}")
coche.acelerar()
coche.acelerar()
coche.acelerar()
print(f"Velocidad Actual {coche.getVelocidad()}")
coche.frenar()
print(f"Velocidad Actual {coche.getVelocidad()}")
coche.setColor("Amarillo")
coche.setModelo("Murcielago")
print(f"Color del Auto: {coche.getColor()}, Modelo: {coche.getModelo()}")
 
#Crear mas objetos
print("#######Coche2#########")
coche2 = Coche()
print(coche2.getColor())
coche2.setColor("Verde")
coche2.setModelo("Gallardo")
