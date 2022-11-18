"""
Ejercicio 2
Crear un script que muestre en pantalla todos los números del 1 al 120
"""
numero_par = 0
for numero_par in range(0,100):
    if numero_par % 2 == 0:
        print(f"{str(numero_par)}")
else:
    print("Ha finalizado el proceso")

numero_par = 1
resultado_str = str(0)
for numero_par in range(1,121):
    if numero_par % 2 == 0:
        resultado_str += "," + str(numero_par)
else:
    print("Ha finalizado el proceso")

print(f"El resultado es: {resultado_str}")
