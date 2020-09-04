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
texto.pack(anchor = E) #Alinea el texto al Este. Ver imagen orientaciones_anchor para mas opciones.
ventana.mainloop()