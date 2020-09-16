from tkinter import *
from PIL import Image, ImageTk #Este modulo antes hay que instalarlo "pip install --upgrade Pillow"

ventana = Tk()
ventana.geometry('500x400')

Label(ventana,text="Hola Gato").pack(anchor=CENTER)

imagen = Image.open('./imagenes/kite.jpg')
render = ImageTk.PhotoImage(imagen)
Label(ventana,image=render).pack()

ventana.mainloop()