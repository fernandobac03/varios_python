"""
Modulos: son funcionalidades ya hechas para reutilizar
En python hay muchos modulos que los puedes consultar:
https://docs.python.org/3/library/

Podemos conseguir modulos que ya vienen en el lenguaje, en internet, o crear nuestros
propios modulos
"""

#importar modulo propio
import mimodulo

print(mimodulo.holaMundo("Fernando"))
print(mimodulo.calculadora(4,2))

#Si yo quiero importar solo una funcion
from mimodulo import holaMundo
print(holaMundo("Carlos"))

#Si quiero importar todas las funciones sin tener que especificar el modulo, al llamar a la funcion
from mimodulo import *
print(holaMundo("Karina"))

#Modulo de fechas
import datetime as dt
print(dt.date.today())
print(dt.datetime.now())

fecha_completa = dt.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d-%m-%y, %H:%M:%S")
print(fecha_personalizada)

print(dt.datetime.now().timestamp())
print(dt.datetime.now().time())


#Modulo de Matem[aticas

import math
print("La raiz cuadrada de 10 es: ", math.sqrt(10))
print("El numero pi:", math.pi)
print("El numero pi en float:", float(math.pi))
print("Redondear:", math.ceil(math.pi))
print("Redondear:", math.floor(math.pi))

#Modulo random
import random

print("N[umero aleatorio entre 15 y 35 es: ", random.randint(15,35))

