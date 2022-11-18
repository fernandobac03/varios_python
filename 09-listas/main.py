"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores bajo un unico nombre
PAra acceder a esos valores podemos usar un indice numerico

"""

pelicula = "Batman"
print(pelicula)

#Definir lista
peliculas = ["Batman", "Espiderman", "El Senior de los Anillos"]
cantantes = list(("Enrique", "Gerardo", "JJ"))
anios = list(range(2020,2050))
variada = ["Fernando", 32, "0105669683", True, 0]


print(peliculas)
print(cantantes)
print(anios)
print(variada)

#Indices,  empiezan en 0

print(peliculas[1])
print(peliculas[-2]) #elementos contando desde el final
print(peliculas[-1]) #elementos contanto desde el final
print(cantantes[1:3]) #Elementos del 1 al
print(cantantes[0:2]) #elementos 0 y 1
print(cantantes[1:])#todos los elementos a partir del indice 1

#modificando un valor de un indice
peliculas[1] = "Falla San Andres"
print(peliculas)

#anadir elementos a una lista

cantantes.append("Maximito")
cantantes.append("Tamayo")
print(cantantes)

#Recorrer una lista para mostrar los diferentes elementos de una lista
print("\n ### Listado de peliculas ###")

nueva_pelicula = ""
while nueva_pelicula != "stop":
    nueva_pelicula = input("Introduce una nueva pelicula: ")
    if nueva_pelicula!="stop":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1} - {pelicula}")


# Listas Multidimensionales
#Lista que contiene otras listas
print("\n ******* Listado de contactos *******")
contactos = [
    ["Antonio", "0999083638", "antonio.abad"],
    ["Fernando", "593665522", "fernando.baculima"],
    ["Karina", "5936555999", "karina.abad"]
]
print(contactos)
print(contactos[1][2])
for contacto in contactos:
    print(contacto[0])

for contacto in contactos:
    for dato in contacto:
        if contacto.index(dato) == 0:
            print(f"Nombre: {dato}")
        else:
            print(f"{dato}")