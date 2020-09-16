"""
Calculadora
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as mb

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter")
ventana.config(bd=25) #Border 25
ventana.geometry("640x480")

nro1 = StringVar()
nro2 = StringVar()

def toFloat(nro):
	try:
		res = float(nro)
	except:
		res = 0
	return res	

def operacion(vl1,vl2,op):
	vl1 = toFloat(vl1)
	vl2 = toFloat(vl2)
	if op == "+":
		res = vl1 + vl2
	elif op == "-":
		res = vl1 -  vl2
	elif op == "*":
		res = vl1 * vl2
	elif op == "/":
		try:
			res = vl1 / vl2
		except Exception as e:
			res = f"Ha ocurrido un error al Dividir {vl1} / {vl2}"
	
	mb.showinfo("Resultado",res)
	nro2.set("") #Limpio el nro2
	nro1.set("") #Limpio el nro1

Label(ventana,text="Primer Numero:").grid(row=0,column=0,padx=10,pady=10)
Entry(ventana,textvariable=nro1).grid(row=0,column=1,sticky=W)
Label(ventana,text="Segundo Numero:").grid(row=0,column=2,padx=10,pady=10)
Entry(ventana,textvariable=nro2).grid(row=0,column=3,sticky=W)

Button(ventana,text="Sumar",command=lambda: operacion(nro1.get(),nro2.get(),"+")).grid(row=1,column=0,pady=5,sticky=W)
Button(ventana,text="Restar",command=lambda: operacion(nro1.get(),nro2.get(),"-")).grid(row=2,column=0,pady=5,sticky=W)
Button(ventana,text="Multiplicar",command=lambda: operacion(nro1.get(),nro2.get(),"*")).grid(row=3,column=0,pady=5,sticky=W)
Button(ventana,text="Dividir",command=lambda: operacion(nro1.get(),nro2.get(),"/")).grid(row=4,column=0,pady=5,sticky=W)
ventana.mainloop()