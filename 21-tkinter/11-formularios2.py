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


ventana.mainloop()