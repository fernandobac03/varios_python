"""
Ejercicio 1.
Un programa que tenga una lista con 8 numeros enteros y que haga lo siguiente
1 Recorrerla y mostrarla
2. Funcion que recorra listas de numeros y devuelva un string
3. Ordenarla y mostrarla
4. Mostrar su longitud
5. Buscar algun elemento (que el usuario pida por teclado)

"""

#Punto 1
miLista = [52,1,36,5,2,9,85,41]
print(miLista)
for numero in miLista:
    print(numero)
else:
    print("Fin de recorrido")

#Punto 2
def recorrerLista(miLista):
    texto = ""
    for numero in miLista:
        texto += str(numero) + " - "
    return texto

print(recorrerLista(miLista))
print(recorrerLista(["Carlos", "Pepe", "Juanito"]))
#Punto 3
miLista.sort()
print(recorrerLista(miLista))

#Punto 4
print(len(miLista))

#Punto 5
numero_a_buscar = int(input("Ingrese el numero que desea buscar en la lista: "))

comprobar = isinstance(numero_a_buscar, int)
if comprobar == True:
    print(numero_a_buscar in miLista)

search = miLista.index(numero_a_buscar)
print("Se encuentra en la posicion: " + str(search))