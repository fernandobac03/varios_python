"""
Ejercicio 5
Crear una lista con el contenido de esta tabla
ACCION      AVENTURA        DEPORTES
GTA         ASSASINS          FIFA 21
COD         CRASH           PRO 21
PUGB        PrinceOfPersa   MOTO GP 21

Mostrar esta informaci[on ordenada,  accion, aventura y deportes
"""

tabla = [
    {
        "categoria":"ACCION",
        "juegos":["GTA", "COD", "PUGB"]
    },
    {
        "categoria":"AVENTURA",
        "juegos":["ASSASINS", "CRASH", "PrinceOfPersa"]
    },
    {
        "categoria":"DEPORTES",
        "juegos":["FIFA 21", "PES 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"------- {categoria['categoria']} ------")
    for juego in categoria['juegos']:
        print(f"Juego: {juego}")
else:
    print("Ha finalizado el recorrido")