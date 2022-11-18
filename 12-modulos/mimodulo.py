
def holaMundo(nombre):
    return f"Hola que tal {nombre}"


def calculadora(numero1, numero2, basicas = False):
    suma = numero1+numero2
    resta = numero1-numero2
    cadena = ""
    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    if basicas != True:
        multiplicacion = numero1*numero2
        division = numero1/numero2
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"

    return cadena