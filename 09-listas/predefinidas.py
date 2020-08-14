cantantes = ["Tupac","Drake","BadBunny","Julio Iglesias"]
numeros = [1,2,3,8,5,4]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Añadir
cantantes.append("Rodrigo")
cantantes.insert(0,"Banda XXI")
print(cantantes)

#Eliminar
cantantes.pop(0)#Eliminar por indice
print(cantantes)
cantantes.remove("Rodrigo")#Eliminar por nombre
print(cantantes)

#Invertir lista
print(numeros)
numeros.reverse()
print(numeros)

#Buscar
print("Drake" in cantantes)
print("Sabroso" in cantantes)

#Contar elementos.
print(cantantes)
print(len(cantantes))

#Cuantas veces aparece un elemento
print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))

#Conseguir indice
cantantes.index("Drake")
print("indice",cantantes.index("Drake"))

#Unir listas
print(cantantes)
cantantes.extend(numeros)
print(cantantes)