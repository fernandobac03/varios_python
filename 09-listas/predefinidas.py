cantantes = ["JJ", "Enrique", "Maximo", "Gerardo"]
numeros = [1,2,5,8,3,4]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Anadir elementos
cantantes.append("Nuevo artista")
print(cantantes)
cantantes.insert(0,"Juan Sequeda")
print(cantantes)

#Eliminar elemmento
cantantes.pop(1)
print(cantantes)

cantantes.remove("Nuevo artista")
print(cantantes)

#Invertir una lista
numeros.reverse()
print(numeros)
cantantes.reverse()
print(cantantes)

#Buscar dentro de una lista
print("Enrique" in cantantes)

#Contar elementos
print(len(cantantes))

#Cuentas veces aparece un elemento
print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))
#conseguir indice
print(numeros)
print(numeros.index(8))

#Unir listas
cantantes.extend(numeros)
print(cantantes)