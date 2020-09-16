from tkinter import *

#Usando la propiedad Side
ventana = Tk()
# ventana.geometry('700x500')

texto = Label(ventana,text = 'Bienvenido a mi programa')
#Configuro el texto
texto.config(
	fg = "white", #Texto Blanco
	bg = "black", #Fondo Negro
	padx = 120, #Margen en X
	pady = 15,
	font = ('Consolas','30')
)
texto.pack(side = TOP)

texto = Label(ventana,text='Mi nombre es Esteban')
texto.config(
	height = 4,
	bg = 'orange',
	font = ('Arial',15)
)
texto.pack(side = TOP, fill = X, expand = YES) #Fill = Rellena en X. Expand = Se expande y ocupa todo.

texto = Label(ventana,text='Basico 1')
texto.config(
	height = 2,
	bg = 'red',
	font = ('Arial',15),
	cursor = 'spider'
)
texto.pack(side= LEFT, fill = X, expand = YES)

texto = Label(ventana, text = 'Basico 2')
texto.config(bg = 'green', height = 2, font = ('Arial',15))
texto.pack(side = LEFT, fill = X, expand = YES)

texto = Label(ventana, text = 'Basico 3')
texto.config(bg = 'yellow', height = 2, font = ('Arial',15))
texto.pack(side = LEFT, fill = X, expand = YES)


ventana.mainloop()