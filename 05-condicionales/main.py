#Condicionales
"""
Estructura de control que permite controlar un flujo de trabajo, si se cumple una condicion, se ejecuta un
flujo, caso contrario se ejecuta otro flujo (grupo de instrucciones)

# Condicional IF
Si se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
Si no:
    Ejecutar otro grupo de instrucciones
if condicion:
    instrucciones
else:
    otras_instrucciones

# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores Lógicos
and = y
or  = o
!   = negación
not = no


"""

# Ejemplo 1
print("######## EJEMPLO 1 ##########")
#color = "verde"
color = input("Ingrese el color: ")
if color=="rojo":
    print("Correcto!")
    print(f"El color es {color}")
else:
    print(f"El color NO es rojo")

# Ejemplo 2
print("######## EJEMPLO 2 ##########")
year = 2020
#year = input("ingrese el año: ")

if int(year) >= 2021:
    print("Estamos de 2021 hacia adelante !!")
else:
    print("año anterior a 2021")

#year = input("ingrese el año: ")
if int(year) < 2021:
    print("Antes que 2021 !!")
else:
    print("Mayor o igual a 2021")

# Ejemplo 3
print("######## EJEMPLO 3 ##########")
nombre = "Fernando Baculima"
ciudad = "Cuenca"
continente = "America"
edad = 17
mayor_edad = 18
if edad  >= mayor_edad:
    #Instrucciones
    print(f"{nombre} SI es mayor de edad")
    if continente == "America":
        print(f"{nombre} SI es Americano")
    else:
        print(f"{nombre} NO es Americano")
else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4
print("######## EJEMPLO 4 ##########")
#1 = lunes, 2 = martes, etc...
dia = 3
#dia = int(input("Ingrese el número del día de la semana: "))
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miercoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    print("Es Fin de semana")
"""
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es Fin de semana")

# Ejemplo 5
print("######## EJEMPLO 5 ##########")
edad_minima = 18
edad_maxima = 65
edad_real = 19
if edad_real >= edad_minima and edad_real <= edad_maxima:
    print("Esta en edad para trabajar!")
else:
    print("NO Esta en edad para trabajar!")

# Ejemplo 6
print("######## EJEMPLO 6 ##########")
pais = "Mexico"
if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print("SI cumplió la condición")
else:
    print("No es un país de habla hispana")

# Ejemplo 7
print("######## EJEMPLO 7 ##########")
pais = "Mexico"
if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print("No es un país de habla hispana")
else:
    print("SI es un país de habla hispana")

# Ejemplo 8
print("######## EJEMPLO 8 ##########")
pais = "BRASIL"
if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print("No es un país de habla hispana")
else:
    print("SI es un país de habla hispana")

print ("foo" if (256).bit_length() > 8 else "bar")





