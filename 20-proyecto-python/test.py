import sqlite3
import hashlib
import usuarios.conexion as cnx
import usuarios.usuario as modelo

# #Conexion SQLite
conectar = cnx.conectar()
database = conectar[0]
cursor = conectar[1]

#Select
cursor.execute("SELECT * FROM NOTAS")

print(cursor.fetchall())

#Muestra info de la tabla
# cursor.execute("PRAGMA table_info(notas)")

# print(cursor.fetchall())
# database.close()
# # cursor.execute("DELETE FROM USUARIOS")
# # database.commit()
# # cursor.execute("SELECT * FROM USUARIOS")
# # print(cursor.fetchall())



# #Pruebo el cifrado
# password = '3marc3110n1'
# passCifrado = hashlib.sha256(password.encode()).hexdigest()
# print(passCifrado)

# #Pruebo el login
# usr = modelo.Usuario('','','emarcelloni@agd.com.ar','3marc3110n1') #Creo el objeto pasando solo email y contraseña
# print(usr.identificar()[3]) #Llamo el metodo identificar.