"""
Funciones predefinidas
"""

nombre = "Fernando Baculima"

#Funciones generales,
# ejm print, type
print(type(nombre))

#Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es un string")

if not isinstance(nombre, float):
    print("La variables no es un nunmero con decimales")

#Limpiar espacios
frase = "       el  contenido"
print(frase)
print(frase.strip())

#Eliminar variables
year = 2022
print(year)
del year
# print(year) #Esta linea lanza error: NameError: name 'year' is not defined

#Comprobar variable vacia
texto = " ff "
if len(texto) <= 0:
    print("La variable est[a vacia")
else:
    print("La variable contiene ", len(texto), " caracteres")

#Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("bella", "genial")
print(nueva_frase)

#Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())