"""
Ejercicio 8
Obtener el % de un número que el valor de porcentaje que introduzca el usuario
¿Cuanto es el x % de un número n?
"""

numero = int(input("Ingrese el número a analizar: "))
porcentaje = int(input(f"Ingrese el porcentaje que desea obtener de {numero}: "))
print(f"El {porcentaje} % de {numero} es: {(porcentaje*numero)/100}")