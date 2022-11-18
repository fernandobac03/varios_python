"""
Ejercicio 10.
El programa debe pedir la nota de 15 alumnos y mostrar en pantalla cuantos han aprobado y cuantos han perdido
"""

aprobados = 0
reprobados = 0

for alumno in range (1,16):
    nota = int(input(f"Ingrese la nota sobre 10 de alumno-{alumno}: "))
    if nota > 12:
        print("Este alumno ha aprobado")
        aprobados += 1
    else:
        print("Este alumno ha reprobado")
        reprobados += 1
else:
    print(f"Total aprobados : {aprobados}")
    print(f"Total reprobados : {reprobados}")