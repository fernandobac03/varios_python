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
    atributo_publico = "Soy atributo publico"
    __atributo_privado = "Soy atributo privado" #Con __ se crean atributos privados

    # El constructur, al invocar la clase se inicializan los valores de los atributos
    # que yo desee inicializar al crear el objeto
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

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
    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca

    def getInfo(self):
        info = "------ Información del coche ---------"
        info += "\n Color " + self.getColor()
        info += "\n Marca " + self.getMarca()
        info += "\n Modelo " + self.getModelo()
        info += "\n Velocidad " + str(self.getVelocidad())
        return info

    #Solo con get se puede obtener o visualizar a propiedades privadas
    def getAtributoPrivado(self):
        return self.__atributo_privado

# Fin definicion clase
