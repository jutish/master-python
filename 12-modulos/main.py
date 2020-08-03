"""Para ver todos los modulos que hay en python googlear python module index
"""

#Importa todas las funciones del archivo referenciado. 
#Es necesario anteponer el nombre del modulo antes de llamar la funcion
import mimodulo 
print(mimodulo.holaMundo("Esteban"))
print(mimodulo.suma(5,4))

#Importa la funcion indicada del modulo "mimodulo"
#No hace falta anteponer el nombre del modulo
from mimodulo import holaMundo
print(holaMundo("Gavilan"))
# print(suma(5,4)) #Daria error

#Importa todas las funciones del modulo referenciado.
#No es necesario poner el nombre del modulo para llamar las funciones.
from mimodulo import *
print(holaMundo("Gavilan"))
print(suma(5,4))

#Modulo Fechas
import datetime
print(datetime.date.today()) #date, es un objeto que tiene la funcion today()
fechaCompleta = datetime.datetime.now() #datetime, es otro objeto que tiene now()
print(fechaCompleta)
print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)
#La funcion strftime (string from time) permite obtener un string formateado de un objeto fecha. 
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior Aqui estan los distintos formatos.
fechaPersonalizada = fechaCompleta.strftime("%d/%m/%Y, %H:%M:%S")
print(fechaPersonalizada)
#Obtengo el timestamp de una fecha. Es el tiempo en Unix "cantidad de segundos transcurridos desde la medianoche UTC del 1 de enero de 1970, sin contar segundos intercalares."
print(fechaCompleta.timestamp())

#Modulo de matematicas.
import math
print(f"Raiz cuadrada de 10: {math.sqrt(10)}")
print(f"Nro. Pi: {math.pi}")
print(f"Redondear {math.ceil(7.51)}") #Redondeo a la alta
print(f"Redondear {math.floor(7.51)}") #Redondeo a la baja

import random
print(f"Nro aleatorio: {random.randint(1,5)}")