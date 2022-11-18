"""
Ejercicio 5.
Mostrar todos los números que se encuentren entre dos números ingresados por el usuario
"""
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numeros = ''

if numero_1<numero_2:
    for numero in range(numero_1,(numero_2+1)):
        numeros += str(numero) + ","
    else:
        print(f"El resultado es: {numeros}")
else:
    print("El número 1 debe ser menor que el número 2")

