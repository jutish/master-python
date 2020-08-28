"""
- Abrir asitente
- Login o Registro
- Registro: Permite crear un usuario
- Login: Permite loguearse
- Una vez logueado podemos crear notas
"""

print("""
Acciones Disponibles:
	-registro
	-login
""")

accion = input('¿Que quieres hacer?: ')
if accion == 'registro':
	print('Vamos a registrarte en el sistema')
elif accion == 'login':
	print('Identificate en el sistema')

