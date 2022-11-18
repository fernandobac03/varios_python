# Programación orientada a objetos (POO / OOP)

# Definir una clase (molde para crear más objetos de ese tipo
# (Coche) con caracteristicas similares

class Coche:

    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad= 300
    caballaje = 500
    plazas = 2

    # Métodos, son acciones que hace el objeto

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad += - 1

    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setModelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo

# Fin definicion clase

# Crear objetos / instanciar la clase
coche = Coche()
print(coche)
print(coche.marca)
print(coche.color)
print(f"Antes de acelerar: {coche.getVelocidad()}")
coche.acelerar()
coche.acelerar()
coche.acelerar()
print(f"Despues de acelerar: {coche.getVelocidad()}")
print(coche.getColor())
coche.setColor("Amarillo")
print(coche.getColor())
print(coche.getModelo())
coche.setModelo("Tigre")
print(coche.getModelo())

# Crear mas objetos
print("Datos de coche 2")
coche2 = Coche()
print(coche2.getColor())

print(type(coche2))