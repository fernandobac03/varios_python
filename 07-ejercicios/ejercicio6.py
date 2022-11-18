"""
Ejercicio 6.
Mostrar todas las tablass de multiplicar del 1 al 10
"""
print("MOSTRANDO TABLAS DE MULTIPLICAR")
for tabla  in range (1,11):
    print("##################")
    print(f"## Tabla del {tabla} ##")
    print("##################")
    for numero in range(1, 11):
        print(f"{tabla} x {numero} = {tabla*numero}")
    print("\n")
else:
    print("Ha finalizado el proceso")

