"""
# FOR
for variable in elemento iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES
"""
contador = 0
resultado = 0
for contador in range(0,10):
    print("Va por el " + str(contador))
    resultado += contador
print("El resultado es: " + str(resultado))

# Ejemplo tablas de multiplicar
print("######## EEMPLO ###########")
numero_usuario = int(input("De qué número quieres ver la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1
print(f"###### Tabla de multiplicar del numero {numero_usuario} ####")
for numero_tabla in range(1,11):
    if numero_usuario == 45:
        print("No se puede mostrar números prohibidos")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")


