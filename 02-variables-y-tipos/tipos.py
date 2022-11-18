nada = None
cadena = "mi nombre es Fernando"
entero = 99
flotante = 4.2
booleano = True
lista = [2,6,5]
listaString = [2,"con string",5]
tuplaNoCAmbia = ("master", "en", "python")
diccionario = {
    "nombre": "Fernando",
    "apellido": "Baculima",
    "web": "mi web"
}
rango = range(5)
dato_byte = b"Probando"

# imprimir variables
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCAmbia)
print(diccionario)
print(rango)
print(dato_byte)
# mostrar tipo de dato
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCAmbia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

texto = "hola soy un texto"
numerito = 756
# me lanzar[a error al imprimir
#print(texto + " " + numerito)

numerito = str(756)
print(texto + " " + numerito)
print(type(numerito))

numerito = int(numerito)
print(type(numerito))

