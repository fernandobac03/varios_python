"""
Capturar excepciones y manejar errores en codigo
susceptible a fallos/errores
"""

try:
    nombre = input("Ingrese su nombre: ")
    if len(nombre)>=1:
        nombre_usuario = f"El nombre es {nombre_usuario}"
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, revisa la varable nombre usuario")
else:
    print("El proceso ha finalizado sin ningun error")
finally:
    print("Fin del proceso")


miLista = [52,1,36,5,2,9,85,41]
numero_a_buscar = 100
try:
    search = miLista.index(numero_a_buscar)
    print("Se encuentra en la posicion: " + str(search))
except:
    print("No existe")



#Multiples excepciones
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print(f"El cuadrado de {numero} es {numero**2}")
except TypeError:
    print("Debes convertir la cadena a entero")
#except ValueError:
#    print("Debes ingresar un numero")
except Exception as e:
    print(type(e))
    print(f"Ha ocurrido un error: {type(e).__name__}")

#Excepciones personalizadas o lanzar excepci[on

try:
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no est[a completo")
    else:
        print("Informaci[on ingresada correctamente")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error", e)