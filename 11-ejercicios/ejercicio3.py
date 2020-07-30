"""
Debe chequear si una variable esta vacia. En caso de estarlo debe llenarla con un texto
en minuscula y mostrarlo en mayuscula
"""

var = ""
if len(var)==0:
	var = "texto en minuscula"
	print(var.upper())
else:
	print(var)

