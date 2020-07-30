"""
Crear un representacion de la siguiente tabla usando lista de diccionario.

ACCION 		AVENTURA		DEPORTE
GTA			 CRASH			 FIFA21
POP			 TOMB RAIDER      PES21
RE7			 CONTRA			 MOTOGP5

Y ordenarla mostrando primero los de accion luego aventura y luego deporte

"""

juegos = [{
			"categoria":"Accion",
			"juegos": ["GTA","POP","R7"]	
		  },
		  {
		  	"categoria":"Aventura",
		  	"juegos": ["CRASH", "TOMB RAIDER", "CONTRA"]
		  },
		  {
			"categoria":"Deporte",
		  	"juegos": ["FIFA21","PES21","MOTOGP5"]
		  }
]

for jg in juegos:
	print(f"Categoria: {jg['categoria']}")
	jg['juegos'].sort()
	print(f"Juegos Ord: {jg['juegos']}")

