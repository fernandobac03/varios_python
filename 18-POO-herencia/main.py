import clases

persona = clases.Persona()
persona.setNombre("Fernando")
persona.setApellido("Baculima")
persona.setAltura("168cm")
persona.setEdad("100")

print("Datos de la persona")
print(persona.getNombre(), persona.getApellido(), persona.getEdad())
print(persona.hablar())

print("-------------")

informatico = clases.Informatico()
informatico.setNombre("John")
informatico.setApellido("Cumbe")
print(f"El informatico es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.caminar())
print(informatico.getLenguajes())
print(informatico.experiencia)

print("-------------")

tecnicoR = clases.TecnicoRedes()

print(tecnicoR.getLenguajes())
print(tecnicoR.auditoria())

