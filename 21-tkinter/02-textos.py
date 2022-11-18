from tkinter import *

ventana = Tk()
#ventana.geometry("1200x750")
texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=40,
    pady=40,
    font=("Arial", 30)

)
texto.pack()

texto = Label(ventana, text="Soy Fernando Baculima")
texto.config(
    width = 20,
    height=10,
    font=("Arial", 18),
    bg = "orange",
    cursor='circle'
)
texto.pack(anchor=W)

texto = Label(ventana, text="Curso Master en Python")
texto.config(
    width = 20,
    height=10,
    font=("Arial", 18),
    bg = "red",
    cursor='spider'
)
texto.pack(side=TOP, fill=X, expand=YES)


ventana.mainloop()

