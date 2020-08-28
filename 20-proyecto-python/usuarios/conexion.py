# import mysql.connector
import sqlite3
#Este metodo se conecta a la base de datos y devuelve un arreglo con la base y el cursor
#Por defecto usa SQLite. Sino se usa MySQL
def conectar(db='SQLite'):
	if db == 'SQLite': #En la oficina uso SQLite porque no puedo instalar MySQL
		#Conexion SQLite
		database = sqlite3.connect('sq_master_python')
		cursor =  database.cursor()
		with open('./sqlite_tables.sql') as sqlite_file:
			sql_script = sqlite_file.read()
		cursor.executescript(sql_script)
	else:
		#Conexion MySQL. En casa uso MySQL
		database = mysql.connector.connect(
			host = 'localhost',
			user = 'emarcelloni',
			password = '3marc3110n1',
			database = 'master_python',
		)
		cursor = database.cursor(buffered = True)

	return [database,cursor]	