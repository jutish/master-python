""""
Listas son colecciones de datos bajo un solo nombre que se acceden usando un indice numerico
"""

pelicula = "batman"
peliculas = ["batman","spiderman","Garfield"]
cantantes = list(("tupac","drake","eminem")) #le debo pasar una Tupla a la funcion list. Es una forma de pasar una tupla a una lista.
years = list(range(2020,2050)) #lista a partir de range
variada = ["Esteban",33,True,list(range(1,5))]
# print(pelicula)
# print(peliculas)
# print(cantantes)
# print(years)
# print(variada)

#Indices
# print(peliculas[1])
# print(peliculas[-2])  #Comineza desde atras
# print(cantantes[1:3]) #Saco una sublista.
# print(cantantes[1:])  #Saco todos los elementos a partir del 1
# print(peliculas)
# peliculas[1] = "Rambo IV"
# peliculas[2] = "El Hobbit"
# print(peliculas)

# #Añadir elementos
# print(cantantes)
# cantantes.append("La Pepa")
# cantantes.append("Dani Guardia")
# print(cantantes)

# #Recorrer una lista con for. y muestra el indice correspondiente.
# # print("\n******Listado peliculas********")
# # for pelicula in peliculas:
# # 	print(f"{peliculas.index(pelicula)}. {pelicula}")


# newFilm=""
# while newFilm != "stop":
# 	newFilm = input("Introduce nueva pelicula: ")
# 	if newFilm!="stop":
# 		peliculas.append(newFilm)

# print("\n******Listado peliculas********")
# for pelicula in peliculas:
# 	print(f"{peliculas.index(pelicula)}. {pelicula}")

#Listas multidimencionales
contactos = [["Esteban Marcelloni","emarcelloni@agd.com.ar"],
			 ["Marcelo Alvarez","malvarez@agd.com.ar"],
			 ["Marcelo Rodeghiero","mrodeghiero@agd.com.ar"]]

# print(contactos)
print(f"Nombre: {contactos[1][0]} y correo: {contactos[1][1]} ")
for ct in contactos:
	for emp in ct:
		if ct.index(emp) == 0:
			print("Nombre: ",emp)
		else:
			print("Correo: ",emp)
	print("\n")

