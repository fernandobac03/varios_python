from io import open
import pathlib
import shutil

#Abrir un archivo
#siempre es recomenda trabajar con rutas absolutas
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

#Escribir dentro de un archivo
archivo.write("******** texto de prueba **********\n")

#Cerrar archivo
archivo.close()

#Abrir archivo, solo para lectura
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo_lectura = open(ruta, "r")

#Leer contenido
contenido = archivo_lectura.read()
print(contenido)

#Leert contenido y guardar en una lista
print("Imprimiendo contenido en lista")

archivo_lectura_lista = open(ruta, "r")

#Leer contenido

lista = archivo_lectura_lista.readlines()
archivo_lectura_lista.close()

print(lista)

for linea in lista:
    lista_linea = linea.split()
    print(lista_linea)
    print(linea.upper())
    print("- " + linea.center(100))


#Copiar archivo

ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
#ruta_alternativa = "../07-ejercicios/fichero_copiado_alternativo.txt"
shutil.copyfile(ruta_original, ruta_nueva)
#shutil.copyfile(ruta_original, ruta_alternativa)

#Mover un archivo
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva_mover = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva_mover)

#Eliminar un archivo
import os
ruta_nueva_mover = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva_mover)

#Comprobar si un archivo existe
print(os.path.abspath("./"))
print(os.path.abspath(".."))

if os.path.isfile("./" + "fichero_copoiado_NUEVO.txt"):
    print("El archivo existe")
else:
    print("El archivo NO existe")

if os.path.isfile(ruta):
    print("El archivo inicial existe")
else:
    print("El archivo inicial NO existe")

if os.path.isfile("ficheros.py"):
    print("El archivo py existe")
else:
    print("El archivo py NO existe")

