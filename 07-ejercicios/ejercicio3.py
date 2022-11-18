"""
# Ejercicio 3
Escribir un script que imprima en pantalla los cuadrados de los 60 números naturales
con while y con for
"""

# FOR
numero = 1
for numero in range (61):
    print(f"El cuadrado de {numero} es: {numero**2}")
else:
    print("Ha finalizado el proceso con for")

# WHILE
numero = 1
while numero <= 60:
    print(f"El cuadrado de {numero} es: {numero**2}")
    numero += 1
else:
    print("Ha finalizado el proceso con while")
