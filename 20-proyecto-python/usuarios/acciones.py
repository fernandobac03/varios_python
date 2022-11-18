#Al importar un paquete se debe importar colocando el path completo del paquete ejm: usuarios.usuario
import usuarios.usuario as modelo
import notas.acciones
class Acciones:


    def registro(self):
        print("\nOk, Vamos a registrarte en el sistema.")
        nombre = input("Ingrese su nombre: ")
        apellidos = input("Ingrese sus apellidos: ")
        email = input("Ingrese su email: ")
        password = input("Ingrese una contraseña: ")

        usuario_instancia = modelo.Usuario(nombre,apellidos, email, password)
        registro = usuario_instancia.registrar()

        if registro[0] >= 1:
            print(f"Hola, {registro[1].nombre }, te has registrado exitosamente con el email {registro[1].email}.")
        else:
            print("Error. Ha habido un error al registrarse, por favor intentelo nuevamente.")


    def login(self):
        print("\nOk, vas a ingresar al sistema.")
        try:
            email = input("Ingrese su email: ")
            password = input("Ingrese una contraseña: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print("Login Incorrecto, por favor, intentalo mas tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota  (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)
        try:
            accion = input("Ingrese el comando que desea ejecutar: ")
            hazEl = notas.acciones.Acciones()

            if accion == "crear":
                print("Vamos a crear una nota")
                hazEl.crear(usuario)
                self.proximasAcciones(usuario)
            elif accion == "mostrar":
                print("Vamos a mostrar una nota")
                hazEl.mostrar(usuario)
                self.proximasAcciones(usuario)
            elif accion == "eliminar":
                print("Vamos a eliminar una nota")
                hazEl.borrar(usuario)
                self.proximasAcciones(usuario)
            elif accion == "salir":
                print(f"Ok {usuario[1]}, adios.")
                exit()
        except Exception as e:
            print(type(e).__name__)
            print(e)

