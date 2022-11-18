"""
Ejercicio 3.
Programa que compruebe si una variable est[a vacia, y si est[a vacia rellenarla con texto
en minusculas y mostrarla en mayusculas
"""

texto = ""
if len(texto.strip())  <= 0:
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido: {texto}")
