from tkinter import *
from tkinter import messagebox as mb

ventana = Tk()
miMenu = Menu(ventana)
ventana.config(menu=miMenu)
ventana.geometry("640x480")
def abrir():
	mb.showinfo("Info","Abrir")
def salir(txt):
	mb.showinfo("Infor",txt)

menuArchivo = Menu(miMenu,tearoff=0) #Tearoff = 0, borra unas lineas punteadas que quedan feo
menuArchivo.add_command(label="Abrir",command=abrir)
menuArchivo.add_command(label="Guardar",command=lambda:salir("Cambios Guardados"))
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir",command=ventana.quit)
menuEditar = Menu(miMenu,tearoff=0)
menuEditar.add_command(label="Copiar")
menuEditar.add_command(label="Pegar")
menuEditar.add_command(label="Cortar")
menuSeleccion = Menu(miMenu,tearoff=0)

miMenu.add_cascade(label="Archivo",menu=menuArchivo)
miMenu.add_cascade(label="Editar",menu=menuEditar)
miMenu.add_cascade(label="Seleccion",menu=menuSeleccion)



ventana.mainloop()