from tkinter import *
import os.path

class Programa:
	
	def __init__(self):
		self.title = 'Master en python en Tkinter'
		self.fav = './imagenes/fav.ico'
		self.fav_alt = './21-tkinter/imagenes/fav.ico'
		self.size = '750x450'
		self.resizable = False

	def cargar(self):
		#Crear ventana principal
		self.ventana = Tk()
		#Cambio el tamaño - 750 de ancho x 450 Alto
		self.ventana.geometry(self.size)
		#Bloquea el tamaño de la ventana, tanto horizontal como vertical. 
		if self.resizable == True:
			self.ventana.resizable(1,1)
		else:
			self.ventana.resizable(0,0)
		#Comprobar si existe un archivo. Obtengo la ruta absoluta
		ruta_icono = os.path.abspath(self.fav)
		#Compruebo si el path corresponde a un archivo
		if not os.path.isfile(ruta_icono):
			ruta_icono = os.path.abspath(self.fav_alt)
		#Mostrar texto en el programa
		texto = Label(self.ventana,text=ruta_icono)
		texto.pack()

		#Icono de la ventana
		self.ventana.iconbitmap(ruta_icono)
		#Titulo de la ventana
		self.ventana.title(self.title)
		
	def addTexto(self,desc):
		texto = Label(self.ventana,text = desc)
		texto.pack()

	def mostrar(self):
		#Arrancar y mostrar la ventana hasta que se cierre
		self.ventana.mainloop()

#Instancio el programa
pr = Programa()
pr.cargar()
pr.addTexto('Hola soy un nuevo texto')
pr.addTexto('Otro texto')
pr.mostrar()

			

