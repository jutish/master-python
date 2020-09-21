"""
Crear un programa que tenga:
- Ventana
- Tamaño Fijo
- No Redimensionable
- Un Menu
- Diferentes Pantallas
- Formulario de añadir producto
- Guardar datos temporalmente en una variable
- Mostrar datos listados en la pantalla
- Opcion Salir
"""

from tkinter import *
from tkinter import ttk
#Definir Ventana
ventana = Tk()
ventana.geometry("640x480")
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0,0)

#Variables de los formularios
productos = []
nameData = StringVar()
priceData = StringVar()

def addPx():
	productos.append([
		nameData.get(),
		priceData.get(),
		addDescEntry.get("1.0","end-1c")
	])
	nameData.set("")
	priceData.set("")
	addDescEntry.delete("1.0","end-1c")
	home() #Me redirijo a la Home
	print(productos)

#Definir campos de pantalla
#Home
homeFrame = Frame(ventana)
homeLabel = Label(homeFrame,text="Inicio")
# Label(homeFrame).grid(row=0) #Solo añado un espacio
productsTable = ttk.Treeview(homeFrame,height=12,columns=2)

#Add
addFrame = Frame(ventana)
addLabel = Label(addFrame,text="Añadir")
addNameLabel = Label(addFrame,text="Nombre del producto:")
addNameEntry = Entry(addFrame,textvariable=nameData)
addPriceLabel = Label(addFrame,text="Precio del producto:")
addPriceEntry = Entry(addFrame,textvariable=priceData)
addDescLabel = Label(addFrame,text="Descripcion")
addDescEntry = Text(addFrame)
boton = Button(addFrame,text="Guardar",command=addPx)

#Info
infoFrame = Frame(ventana)
infoLabel = Label(infoFrame,text="Info")
infoLabelData = Label(infoFrame,text="Creado por Esteban Marcelloni")

#Pantallas
def home():
	cls()
	homeLabel.config(
		fg="white",
		bg="black",
		font=("Arial",30),
		padx=280,
		pady=20
	)
	homeLabel.grid(row=0,column=0,columnspan=20)

	productsTable.heading("#0",text="Producto")
	productsTable.heading("#1",text="Precio")

	productsTable.grid(pady=5)

	# if len(productos)>0:
	# 	px = productos[-1] #Siempre me quedo con el ultimo producto añadido. Si esta vacio da error.
	# 	Label(homeFrame,text=px[0]).grid(sticky=W) #Nombre
	# 	Label(homeFrame,text=px[1]).grid(sticky=W) #Precio
	# 	Label(homeFrame,text=px[2]).grid(sticky=W) #Descripcion
	# 	Label(homeFrame,text="------------------").grid(sticky=W)

	if len(productos)>0:
		px = productos[-1] #Siempre me quedo con el ultimo producto añadido. Si esta vacio da error.
		productsTable.insert('',0,text=px[0],values=(px[1]))

	homeFrame.grid()

def add():
	cls()
	#Encabezado
	addLabel.config(
		fg="white",
		bg="black",
		font=("Arial",30),
		padx=270,
		pady=20
	)
	addLabel.grid(row=0,column=0,columnspan=20)
	#Campos del formulario
	addNameLabel.grid(row=1,column=0,sticky=W,pady=5)
	addNameEntry.grid(row=1,column=1,sticky=W,pady=5)
	addPriceLabel.grid(row=2,column=0,sticky=W,pady=5)
	addPriceEntry.grid(row=2,column=1,sticky=W,pady=5)
	addDescLabel.grid(row=3,column=0,sticky=W,pady=5)
	addDescEntry.config(width=30,height=5)
	addDescEntry.grid(row=3,column=1,sticky=W,pady=5)
	boton.config(bg="green",fg="white",padx=10)
	boton.grid(row=4,column=1,sticky=E,padx=15,pady=5)
	addFrame.grid()

def info():
	cls()
	infoLabel.config(
		fg="white",
		bg="black",
		font=("Arial",30),
		padx=290,
		pady=20
	)
	infoLabel.grid(row=0,column=0,columnspan=20)
	infoLabelData.grid(row=1,columnspan=20)
	infoFrame.grid()

#Limpio la pantalla antes de agregar otro elemento
def cls():
	addFrame.grid_remove()
	homeFrame.grid_remove()
	infoFrame.grid_remove()




home()

#Menu Superior
miMenu = Menu(ventana)
miMenu.add_command(label="Inicio",command=home)
miMenu.add_command(label="Añadir",command=add)
miMenu.add_command(label="Informacion",command=info)
miMenu.add_command(label="Salir",command=ventana.quit)
#Cargar Menu
ventana.config(menu=miMenu)





ventana.mainloop()