"""
Una variable es un contenedor de informacion que dentro guardar[a un dato, se pueden creaer
muchas variables y que cada una tenga un dato distinto.
"""


# CREAR VARIABLES
texto = "la informaci[on de mi variable texto"
texto = 1
texto2 = "Fernando Baculima"
numero = 45
decimal = 6.5

# MOSTRAR VALOR DE LAS VARIABLES
print(texto)
print(texto2)
print(numero)
print(decimal)
print("------------")
numero = 87
decimal = 1.7
print(numero)
print(decimal)
print("------------")

# CONCATENACION
nombre = "Fernando"
apellido = "Baculima"
web = "fernandobac.com"
print(nombre, apellido, web)
print("Hola, mi nombre es" + nombre + " " +  apellido + " - " + web)
print(f"Hola, mi nombre es {nombre} {apellido} - {web}")
print("Hola, mi nombre es {} {} y mi web es: {}".format(nombre, apellido, web))

