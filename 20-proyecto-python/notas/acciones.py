import notas.notas as modelo

class Acciones:
    def crear(self, usuario):
        print(f"Ok, {usuario[1]}, se va a crear una nueva nota...")
        titulo = input("Ingresa el titulo de la nota: ")
        descripcion = input("Ingresa la descripcion de la nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0]>=1:
            print(f"Perfecto, se ha guardado la nota de titulo: {nota.titulo}")
        else:
            print(f"{usuario.nombre}, no se ha guardado la nota")
        return True

    def mostrar(self, usuario):
        print(f"Ok {usuario[1]}, Aqui tienes tus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print("------------------------")
            print(nota[2]," - ", nota[3])

    def borrar(self,usuario):
        print(f"Ok {usuario[1]}, se procede a borrar la nota")

        titulo = input("Ingresa el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        try:
            eliminar = nota.eliminar()
            if eliminar[0] >= 1:
                print(f"Se ha borrado la nota de titulo {titulo}")
            else:
                print("No se ha borrado la nota")
        except Exception as e:
            print(type(e))
            print(e)
