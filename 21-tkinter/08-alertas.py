from tkinter import *
from tkinter import messagebox as mb

def sacarAlerta(type="info",msj=""):
	if type=="info":
		mb.showinfo("Info",msj)
	elif type=="warning":
		mb.showwarning("Warning",msj)
	else:
		mb.showerror("Error",msj)

def salir(msj):
	res = mb.askquestion("Salir","¿Esta seguro que desea salir?")
	if res=="yes":
		sacarAlerta("info",msj)
		ventana.destroy()#cierra la ventana que invoca el metodo.
		# exit() #cierra todo el programa
		
ventana = Tk()
ventana.geometry("640x480")

#Para pasar un parametro en un boton debo usar lambda, el cual crea una funcion anonima la cual a su vez
#llama a mi funcion, ej: sacarAlerta("Warning"), de esa forma puedo pasar parametros.
Button(ventana,text="Enviar",command=lambda: sacarAlerta("Warning")).grid(row=0,column=1,pady=5,padx=5)
Button(ventana,text="Salir",command=lambda: salir(f"Adios Esteban")).grid(row=1,column=1,pady=5,padx=5)

ventana.mainloop()