import os, shutil, pathlib

#Crear carpeta verificao si existe o no el directorio
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("El directorio ya existe")

#Eliminar el directorio
#os.rmdir("./mi_carpeta")

#Copiar un directorio
ruta_original = "./mi_carpeta"
ruta_destino = "./micarpeta_copia"
#shutil.copytree(ruta_original, ruta_destino) #lanza error cuando ya existe el directorio

#Listar los archivos dentro de una carpeta
ruta = str(pathlib.Path().absolute()) + "/creada_manualmente"
print("mostrdo el contenido de mi carpeta")
contenido_directorio = os.listdir(ruta)
for fichero in contenido_directorio:
    print(fichero)