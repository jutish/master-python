import os,shutil

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
	os.mkdir("./mi_carpeta")
else:
	print("Ya existe el directorio")	

#Eliminar carpeta
# os.rmdir("./mi_carpeta")	

#Copiar carpeta
rutaOrigen = "./mi_carpeta"
rutaDestino = "./mi_carpeta_copia"
shutil.copytree(rutaOrigen,rutaDestino)

#Listar Carpeta
contenido = os.listdir("./mi_carpeta")
print(contenido)
for ct in contenido:
	print(ct)
