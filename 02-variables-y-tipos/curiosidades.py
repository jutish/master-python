mi_text = '"hola" gente' #si mi Strin lo defino con comillas dobles o simples, luego dentro puedo usar las contrarias
mi_texto2 = "mi \"segundo\" texto" #Tambien puedo usar \ para escapar la funcionalidad de la comilla.
mi_texto3 = "mi 'tercer' texto"
# print(mi_text)

texto_unido = mi_text + "\n" + mi_texto2 #salto de linea
print(texto_unido)
texto_unido = mi_text + "\t" + mi_texto2 #tabulacion
print(texto_unido)
texto_unido = mi_text + "\r" + mi_texto2 #borra lo que precede a la barra
print(texto_unido)