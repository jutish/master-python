from io import open
import pathlib
import shutil
import os

#Abrir archivo/fichero
# archivo = open("./14-sistema-arhivo/fichero_texto.txt","a+") #Asi no lo encuentra, no le gusta la ruta relativa.
# archivo = open("fichero_texto.txt","a+") #Asi SI lo encuentra. Si no existe lo Crea.
rutaAbs = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(rutaAbs,"a+")
#Escribir en un archivo.
archivo.write("***Soy un texto metido desde python****\n")
archivo.write("***Soy un texto metido desde python****\n")
#Cerrar archivo
archivo.close()

#Abrir solo lectura
rutaAbs = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivoLectura = open(rutaAbs,"r")
contenido = archivoLectura.read() #Este read() lee todo el archivo. El puntero quedo al final.
print(contenido)

#Leer contenido y guardarlo en lista
lista = archivoLectura.readlines() #Este readlines() lee cada linea. Si antes se ejecutro read() no lee nada, porque el puntero esta al final.
archivoLectura.close()
for el in lista:
	print(el)
	

#Copiar archivo
# rutaOrigen = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# rutaDestino = str(pathlib.Path().absolute()) + "/fichero_texto_copia.txt" #Lo copia en el mismo directorio.
# rutaDestinoFuera = str(pathlib.Path().absolute()) + "/../13-paquetes/fichero_texto_cop2.txt" #Salgo con ../ y lo copio en otra carpeta
# print(rutaDestino)
# print(rutaDestinoFuera) 
# shutil.copyfile(rutaAbs,rutaDestino)
# shutil.copyfile(rutaAbs,rutaDestinoFuera)

#Mover Archivo
rutaOrigen = str(pathlib.Path().absolute()) +"/fichero_texto.txt"
rutaDestino = str(pathlib.Path().absolute()) + "/fichero_texto_movido.txt"
shutil.move(rutaOrigen,rutaDestino)

#Eliminar archivo
os.remove(rutaDestino)
#Verificar si existe un archivo
if os.path.isfile("./fichero_texto.txt"):
	print("El archivo existe")
else:
	print("El archivo no existe")	

	










