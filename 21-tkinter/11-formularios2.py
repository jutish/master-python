from tkinter import *

ventana = Tk()
ventana.geometry("640x480")

encabezado = Label(ventana,text="Formularios 2")
encabezado.config(
	padx=15,
	pady=15,
	fg="white",
	bg="green",
	font=("consolas",20)
)
encabezado.grid(row=0,column=0,columnspan=6)

web = IntVar()
mobile = IntVar()
profesion = StringVar()
#Botones check
Label(ventana,text="¿A que te dedicas?").grid(row=1,column=0)
Label(ventana,textvariable=profesion).grid(row=1,column=1)

Checkbutton(ventana,
	text="Desarrollo Web",
	variable=web,
	onvalue=1,
	offvalue=0,
	command=lambda: mostrar("Desarrollo Web")).grid(row=2,column=0,sticky=W)
Checkbutton(ventana,
	text="Desarrollo Mobile",
	variable=mobile,
	onvalue=1,
	offvalue=0,
	command=lambda:mostrar("Desarrollo Mobile")).grid(row=3,column=0,sticky=W)

def mostrar(txt):
	if web.get()==True or mobile.get()==True:
		profesion.set(profesion.get()+" "+txt)
	else:
		profesion.set("")

#Radio Button
opcion = StringVar()
Label(ventana,text="¿Cuál es tu genero?").grid(row=5)
rd1=Radiobutton(ventana,
			text="Masculino",
			value = "Masculino",
			variable=opcion)
rd1.grid(row=6)

rd2=Radiobutton(ventana,
			text="Femenino",
			value="Femenino",
			variable=opcion,
			)
rd2.grid(row=7)
rd1.select()
rd2.deselect()
Label(ventana,textvariable=opcion).grid(row=8)


#OptionMenu
Label(ventana,text="Selecciona una opcion: ").grid(row=9)
opcionMenu = StringVar()
opcionMenu.set("Op1")
select = OptionMenu(ventana,opcionMenu,"Op1","Op2","Op3","Op4")
select.grid(row=10)
ventana.mainloop()