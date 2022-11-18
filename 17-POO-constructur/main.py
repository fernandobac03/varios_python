from coche import Coche

carro = Coche("negro", "renaukt", "clio", 500, 200, 4)

print(carro.getColor())
print(carro.getInfo())

carro1 = Coche("Amarillo", "chevrolet", "vitara", 300, 280, 4)
carro2 = Coche("Verde", "hiunday", "ix", 200, 100, 2)
carro3 = Coche("Gris", "ford", "ranger", 800, 350, 6)

print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado
if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto correcto")

# Visibilidad -- propiedades o metodos privados
print(carro1.atributo_publico)
print(carro1.getAtributoPrivado()) #Solo con get se puede visualizar un atributo privado
