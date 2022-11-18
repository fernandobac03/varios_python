"""
Ejercicio 4.
Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano
y que imprima un mensaje segun el tipo de dato de cada variable
"""

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
    return result


def comprobarTipado(dato, tipoDato):
    test = isinstance(dato,tipoDato)
    result = ""
    if test:
        result = f"Este dato es del tipo {traducirTipo(tipoDato)}"
    else:
        result = "No valid'o correctamente"
    return result

miLista = ["Hola mundo", 330]
titulo = "Master en python"
numero = 100
miBooleano = True

print(comprobarTipado(miLista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(miBooleano, bool))
print(comprobarTipado(miBooleano, str))
