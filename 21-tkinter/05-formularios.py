"""
En este ejemplo usamos grid() en lugar de pack(). Para posicionar los elementos en la ventana.
En grid cada elemento se organiza como si fueze justamente una grilla, es decir usando filas y columnas.
"""

from tkinter import *

ventana = Tk()
ventana.geometry("600x400")
ventana.title("Formularios")

#Texto encabezado
encabezado = Label(ventana,text="Formularios con Tkinter")
encabezado.config(
	fg="white",
	bg="darkgrey",
	font=("Open Sans",18),
	pady=10
)
encabezado.grid(row=0,column=0,columnspan=12,sticky=W) #Usamos Grid en lugar de Pack. 

#Label para el campo
Label(ventana,text="Nombre").grid(row=1,column=0,sticky=W,padx=2,pady=2)
#Creo campo de texto
campo = Entry(ventana)
campo.config(justify="left",state="disabled") #Seteo la justificacion del texto y si esta deshabilitado.
campo.grid(row=1, column=1,padx=2,pady=2,sticky=W)

#Label para el campo
Label(ventana,text="Apellidos").grid(row=2,column=0,sticky=W,padx=2,pady=2)
#Creo campo de texto
Entry(ventana).grid(row=2, column=1,padx=2,pady=2,sticky=W)

#Label para el campo descripcion.
Label(ventana,text="Descripcion").grid(row=3, column=0, sticky=NW, padx=2, pady=2)
#Creo un campo de texto grande
txtArea = Text(ventana)
txtArea.config(width=30,height=5,font=("Arial",12))
txtArea.grid(row=3,column=1,padx=2,pady=2,sticky=W)

#Botones
boton = Button(ventana,text="Enviar")
boton.config(bg="green",fg="white",padx=10,pady=5) #El padding dentro del boton modifica el tamaño.
boton.grid(row=4, column=1,sticky=W,pady=15)#El padding en el grid(), modifica la separacion.

ventana.mainloop()