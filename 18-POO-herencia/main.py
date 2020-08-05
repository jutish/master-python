import clases

persona = clases.Persona()
persona.setNombre("Esteban")
persona.setApellidos("Marcelloni")
persona.setAltura("170 cm")
persona.setEdad("33 Años")
print(f"La Persona es: {persona.getNombre()}, {persona.getApellidos()}")

informatico = clases.Informatico()
informatico.setNombre("Gavilan")
informatico.setApellidos("Stefoni")
informatico.setAltura("175 cm")
informatico.setEdad("34 años")

print(f"El informatico es: {informatico.getNombre()}, {informatico.getApellidos()}")
print(f"El sabe: {informatico.getLenguajes()}")

tecnico = clases.TecnicoRedes()
print(tecnico.getLenguajes())


