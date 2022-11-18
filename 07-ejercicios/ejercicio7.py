"""
Ejercicio 7.
HAcer un programa que muestre todos los números impares entre dos números ingresados por el usuario.
"""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

print("Imprimiendo números pares")

if numero_1<numero_2:
    for numero in range(numero_1, (numero_2+1)):
        if numero%2 ==0:
            print(f"{numero} es PAR")
        else:
            print(f"{numero} es IMPAR")
    else:
        print("El proceso ha finalizado")
else:
    print("El primer número debe ser menor que el segundo número")