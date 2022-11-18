"""
Diccionario:
Tipo de datos que almacena un conjunto de datos.
En formato clave - valor
Es parecido a un array asociativo o un objeto json

"""

persona = {
    "Nombre": "Fernando",
    "Apellido": "Baculima",
    "web":"fernando.baculima"

}

print(persona)
print(type(persona))
print(persona["Apellido"])

# Lista con diccionarios

contactos = [
    {
        "Nombre": "Fernando",
        "email": "fernando.baculima@out.com"
    },
    {
        "Nombre": "Luis",
        "email": "luis.colombia@out.com"
    },
   {
        "Nombre": "Salvador",
        "email": "salvador.honduras@out.com"
    }
]

print(contactos)
print(contactos[0]["Nombre"])
#modificando un valor
contactos[0]["Nombre"] = "John"
print(contactos[0]["Nombre"])

for contacto in contactos:
    print("---------------------")
    print(f"Nombre del contacto: {contacto['Nombre']}")
    print(f"Email: {contacto['email']}")