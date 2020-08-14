"""
Pedir la nota de 15 alumnos y sacar por pantalla cuantos aprobaron
y cuantos desaprobaron
"""
notaMin = 6
cont = 0
acuAp = 0
acuDe = 0

for cont in range(1,16):
	nota = int(input(f"Ingrese Nota Alumno {cont}: "))
	if nota >= notaMin:
		acuAp += 1
	else:
		acuDe += 1

print(f"Alumnos aprobados: {acuAp} ")
print(f"Alumnos reprobados: {acuDe} ")