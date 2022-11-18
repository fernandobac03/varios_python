
#Una buen practica es siempre retornar valores en las funciones
#Utilizar parametros
def miFuncion(nombre):
    return("Hola que tal "+ nombre)

def miSegundaFuncion(apellido):
    return("Hola que tal 2 " + apellido)

nombre = "Fernando"
apellido = "Baculima"

print("Hola Mundo")
print(f"Bienvenido {nombre}")

#Ejecutar las funciones despues de la definicion de las variables, caso contrario lanza error
print(miFuncion(nombre))
print(miSegundaFuncion(apellido))

