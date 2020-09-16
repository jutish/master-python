 from tkinter import *

ventana = Tk()
ventana.title("Mi Formulario")
ventana.geometry("640x480")

nombre = StringVar()
res = StringVar()
def setDato():
	res.set(nombre.get())

Label(ventana,text="Nombre:").grid(row=0,column=0,sticky=W,padx=10,pady=5)
Entry(ventana,textvariable=nombre).grid(row=0,column=1,padx=10)

Label(ventana,text="Resultado: ").grid(row=1, column=0,sticky=W,padx=10,pady=5)
Label(ventana,textvariable=res).grid(row=1,column=1,sticky=W,padx=10,pady=5)
Button(ventana,text="Enviar",command=setDato).grid(row=2,column=0,pady=5,sticky=W,padx=10)




ventana.mainloop()
