"""
Tenemos un tipo de dato clave:valor.
La clave puede ser alfanumerico
"""

# persona = {
# 	"nombre":"Esteban",
# 	"apellido": "Marcelloni",
# 	"web":"www.emarcelloni.com"
# }

# print(persona)
# print(type(dict))
# print(persona["apellido"]) #Como acceder a los datos.

#Lista con diccionarios
contactos = [
			{
			'nombre':"Esteban",
			'email':"emarcelloni@agd.com"
			},
			{
			'nombre':"Gavilan",
			'email':'gav@gmail.com'
			}
]

# print(contactos)
# print(contactos[0]["nombre"])
# contactos[0]["nombre"] = "Esteban Marcelloni"
# print(contactos[0]["nombre"])
for ct in contactos:
	print(f"Nombre: {ct['nombre']}")
