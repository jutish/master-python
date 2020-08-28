import sqlite3

#Conexion SQLite
database = sqlite3.connect('sq_master_python')
cursor =  database.cursor()
cursor.execute("SELECT * FROM USUARIOS")
print(cursor.rowcount)
print(cursor.fetchall())

