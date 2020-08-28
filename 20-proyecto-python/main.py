"""
- Abrir asitente
- Login o Registro
- Registro: Permite crear un usuario
- Login: Permite loguearse
- Una vez logueado podemos crear notas
"""
from usuarios import acciones 

acc = acciones.Acciones()
print("""
Acciones Disponibles:
	-registro
	-login
""")
accion = input('¿Que quieres hacer?: ')
if accion == 'registro':
	acc.registro()
elif accion == 'login':
	acc.login()

