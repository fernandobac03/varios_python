"""
Tkinter
Modulo para crear interfaces graficas de usuario
"""

from tkinter import *
import pathlib
import os.path

class Programa:
    def __init__(self):
        self.title = "Master en Python con Fernando Baculima"
        self.icon = os.path.abspath("images/Favicon.ico")
        self.size = "700x470"
        self.resiable = True

    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.title)
        # Comprobar si existe el archivo

        if os.path.isfile(self.icon):
            print("ok")

        # Mostrar texto en el programa
        texto = Label(ventana, text=str(self.icon))
        texto.pack()

        # ventana.iconbitmap(r'/home/abac/curso_python/21-tkinter/images/Favicon.ico')

        imgicon = PhotoImage(file=self.icon)
        ventana.tk.call('wm', 'iconphoto', ventana._w, imgicon)

        # Dimensionar la ventana
        ventana.geometry(self.size)

        # bloquear el tamanio de la ventana
        if self.resiable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0,0)

        # ventana.resizable(valor,valor) 0,0 para bloquear ancho y alto, 1,0 para bloquear solo ancho - 0,1 para bloquear solo alto - 1,1 para activar modificar ancho y alto



    def addTexto(self, texto=""):
        texto = Label(self.ventana, text = texto)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

programa = Programa()
programa.cargar()
programa.addTexto("Hola desde Primera linea")
programa.addTexto("Segunda Linea")

programa.mostrar()