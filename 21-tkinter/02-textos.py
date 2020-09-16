from tkinter import *

ventana = Tk()
ventana.geometry('700x500')

texto = Label(ventana,text = 'Bienvenido a mi programa')
#Configuro el texto
texto.config(
	fg = "white", #Texto Blanco
	bg = "black", #Fondo Negro
	padx = 120, #Margen en X
	pady = 15,
	font = ('Consolas','30')
)
texto.pack()

texto = Label(ventana,text='Mi nombre es Esteban Marcelloni')
texto.config(
	height = 4,
	bg = 'orange',
	font = ('Arial',15)
)
texto.pack(anchor = CENTER) #Alinea el texto al Este. Ver imagen orientaciones_anchor para mas opciones.

texto = Label(ventana,text='Otro Texto')
texto.config(
	height = 2,
	bg = 'red',
	font = ('Arial',15),
	cursor = 'spider'
)
texto.pack(anchor = E)

ventana.mainloop()