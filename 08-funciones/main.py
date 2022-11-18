"""
funciones, una función es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse incovando a la función tantas veces como sea necesario

#Creando la función
def nombreDeMiFuncion(parametros):
    #Bloque de código / conjunto de instrucciones

#Invocando a la función
nombreDeMiFuncion(mi_parametro)

"""

#Ejemplo 1
print("#####  Ejemplo 1 #####")

#Definiendo una función
def muestraNombres():
    print("Fernando")
    print("Carlos")
    print("Karina")
    print("Alexandra")
    print("\n")

#Invocando a la función
muestraNombres()
muestraNombres()

#Ejemplo 2
print("#####  Ejemplo 2 #####")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Eres mayor de edad")
mostrarTuNombre("Fernando",9)
mostrarTuNombre("Baculima",19)
#nombre = input("Introduce tu nombre: ")
#edad = int(input("Introduce tu edad: "))
#mostrarTuNombre(nombre, edad)

#Ejemplo 3
print("#####  Ejemplo 3 #####")

def tablaMultiplicar(tabla):
    print(f"Tabla de mulitplicar del {tabla}")
    for numero in range (1,11):
        print(f"{tabla} X {numero}  = {tabla * numero}")
    else:
        print("Ha finalizado el proceso.")
    print("\n")
tabla = int(input("Ingrese el numero para la tabla de multiplciar: "))
tablaMultiplicar(tabla)

#Ejemplo 3.1, imprimiento todas las tablas de multiplicar del 1 al 10
for numero_tabla in range (1,11):
    tablaMultiplicar(numero_tabla)
else:
    print("Ha finalizado todas las Tablas")

#Ejemplo 4
print("#####  Ejemplo 4 #####")

#parametrps funcionales, incluye parametros que son opcionales
def getEmpleado(nombre, id = None):#para que sea opcional se debe colocar un valor por default
    print("EMPLEADO")
    print(f"Nombre {nombre}")
    if id != None:
        print(f"ID {id}")
getEmpleado("Fernando", "0203050607")
getEmpleado("Carlos")  # El segundo parametro es opcional

#Ejemplo 5: parametros opcionales y return o devoluci[on de datos
print("#####  Ejemplo 5 #####")

def saludarme(nombre):
    saludo = f"Hola {nombre}"
    return saludo
print(saludarme("Fernando Baculima C"))

#Ejemplo 6, calculadora con parametro opcional
print("#####  Ejemplo 6 #####")

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

print(calculadora(5,3, True))
print(calculadora(3,1))

#Ejemplo 7, funcionaes dentro de otras funciones
print("#####  Ejemplo 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto
print(getNombre("Fernando"), getApellido("Baculima"))

def getNombreYApellido(nombre, apellido):
    texto = getNombre(nombre) + " " + getApellido(apellido)
    return(texto)
print(getNombreYApellido("Fernando", "Baculima C"))

#Ejemplo 8, funcionaes lambda, es una funcion anonima,
print("#####  Ejemplo 8 #####")

# Es decir que no se define con un nombre, todo su contenido se traduce en una linea en el c[odigo

dime_el_year = lambda year: f"El anio es {year *10}"

print(dime_el_year(2034))
