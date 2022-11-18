"""
Variable locales, se definen dentro de la funcion y no se pueden utilizar
fuera de ella, solo est[an disponibles dentro.
A no ser que hagamos un return.

Variable Global: Son las que se declaran fuera de una funcion
y est[an disponibles dentro y fuera de ellas.

"""

#Variables Global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)

def holaMundo():
    frase = "Hola Mundo" #La variable se llama igual que la global, pero es diferente, es local
    print("Variable dentro de la funcion")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "fernandobaculima.com"
    print(f"Imprimiendo dentro de la funcion: {website}")

def holaMundo2():
    #frase = "Hola Mundo"
    print(frase) #Toma el valor de la Global

holaMundo()
holaMundo2()
print(f"Imprimiendo fuera de la funcion: {website}")


