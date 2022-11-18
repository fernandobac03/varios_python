"""
Ejercicio 9.
Hacer un programa que pida números al usuario indefinidamente hasta que ingrese 111
"""

numero_ingresado = 0

while numero_ingresado != 111:
   numero_ingresado = int(input("Ingrese un número: "))
   print(f"Has introducido el: {numero_ingresado}")
else:
    print("Proceso finalizado")