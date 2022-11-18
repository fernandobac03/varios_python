"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, indentifica al usuario y nos preguntará los datos de ingreso
- Crear nota, mostrar notas, borrarlas
"""

from usuarios import acciones
print("""
Acciones disponibles:
    -registro
    -login
    -exit
""")

#Instanciando la clase de acciones
ejecutarAccion = acciones.Acciones()

accion = ""
while(accion!='exit'):
    accion = input("Qué acción deseas hacer?: ")
    if accion=='registro':
        ejecutarAccion.registro()
        break;

    elif accion=='login':
        ejecutarAccion.login()
        break;

    else:
        print("Por favor, ingrese una opción correcta, si desea salir, ingrese exit.")
else:
    print("Gracias por visitarnos. Adios")

