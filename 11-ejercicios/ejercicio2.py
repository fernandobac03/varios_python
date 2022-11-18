"""
Ejercicio 2.
Escribir un programa que anada valores a una lista mientras su longitud sea menor a 10
Usar while y for
"""

miLista = []

while len(miLista) < 10:
    elemento_nuevo = input("Ingrese el elemento: ")
    miLista.append(elemento_nuevo)
else:
    print("Ha finalizado el proceso con while")
    print(miLista)
miLista2 = []
for contador in range(0,10):
    elemento_nuevo = input("Ingrese el elemento: ")
    miLista2.append(elemento_nuevo)
else:
    print("Ha finalizado el proceso con for")
    print(miLista2)