from tkinter import *
from tkinter import messagebox as mb


"""
Calculadora
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar resultado en una alerta
"""



class Calculadora:

	def __init__(self):
		self.nro1 = StringVar()
		self.nro2 = StringVar()
		self.ventana = Tk()
		self.ventana.title("Ejercicio completo con Tkinter")
		self.ventana.config(bd=25) #Border 25
		self.ventana.geometry("640x480")
	
		Label(ventana,text="Primer Numero:").grid(row=0,column=0,padx=10,pady=10)
		Entry(ventana,textvariable=nro1).grid(row=0,column=1,sticky=W)
		Label(ventana,text="Segundo Numero:").grid(row=0,column=2,padx=10,pady=10)
		Entry(ventana,textvariable=nro2).grid(row=0,column=3,sticky=W)
		Button(ventana,text="Sumar",command=lambda: self.operacion(self.nro1.get(),self.nro2.get(),"+")).grid(row=1,column=0,pady=5,sticky=W)
		Button(ventana,text="Restar",command=lambda: self.operacion(self.nro1.get(),self.nro2.get(),"-")).grid(row=2,column=0,pady=5,sticky=W)
		Button(ventana,text="Multiplicar",command=lambda: self.operacion(self.nro1.get(),self.nro2.get(),"*")).grid(row=3,column=0,pady=5,sticky=W)
		Button(ventana,text="Dividir",command=lambda: self.operacion(self.nro1.get(),self.nro2.get(),"/")).grid(row=4,column=0,pady=5,sticky=W)
		ventana.mainloop()
	
	
	def toFloat(self,nro):
		try:
			res = float(nro)
		except:
			res = 0
		return res	
	
	def operacion(self,vl1,vl2,op):
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
	

