# Herencia: Es la posibilidad de compartir atributos o metodos entre clases
# y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellido
    altura
    edad
    """

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getAltura(self):
        return self.edad

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

#LA siguiente clase hereda de la clase persona
class Informatico(Persona):

    """
    lenguajes
    experiencia
    """

    def __init__(self, lenguajes = "HTML, PYTHON, CSS", experiencia = 5):
        self.lenguajes = lenguajes
        self.experiencia = experiencia

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes): #El setter de lenguajes
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "He reparado el ordenador"

class TecnicoRedes(Informatico):

    def __init__(self, auditarRedes = "Experto", experienciaRedes = 15):
        super().__init__() #para que la clase hija tambien ejecute el constructor de la clase padre, caso contrario no ejecutar'a ese constructor
        self.auditarRedes = auditarRedes
        self.experienciaRedes = experienciaRedes

    def auditoria(self):
        return "Estoy auditando una red"