class Coche:
	color = "Rojo"
	marca = "Ferrari"
	modelo = "Aventador"
	velocidad = 300
	caballaje = 500
	plazas = 2

	soy_publico = "Soy un atrr. publico"
	__soy_privado = "Soy un atrr. privado" #Que sea privado lo define __nombre Es decir doble __ solo al inicio.

	def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
		self.color = color
		self.marca = marca
		self.modelo = modelo
		self.velocidad = velocidad
		self.caballaje = caballaje
		self.plazas = plazas

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

	def setMarca(self,marca):
		self.marca = marca

	def getMarca(self):
		return self.marca

	def getInfo(self):
		info = "---Info del Coche---" 
		info += "\n Color: " + self.getColor()
		info += "\n Marca: " + self.getMarca()	
		info += "\n Modelo: " + self.getModelo()	
		info += "\n Velocidad: " + str(self.getVelocidad())
		return info

	def getPrivado(self):
		return self.__soy_privado	
