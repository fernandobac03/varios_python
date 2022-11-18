# Importar modulo
import sqlite3

#Conexi[on
conexion = sqlite3.connect("pruebas.db")

# Cursor, permitir[a ejcutar consultas
cursor = conexion.cursor()

#Crear Tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos ( 
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               titulo VARCHAR(255), 
               descripcion text,
               precio int(255)
               )""")

#Guardar cambios
conexion.commit()

## Insertar datos
#cursor.execute(" INSERT INTO productos" +
#               " VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")

#Guardar cambios
conexion.commit()

#Listar datos
cursor.execute("Select * from productos")
print(cursor)
productos = cursor.fetchall()
print(productos)
for producto in productos:
    print(f"Producto-{productos.index(producto)} : {producto}")

cursor.execute("Select titulo from productos")
producto_primero = cursor.fetchone()
print(producto_primero)

#borrar todo
cursor.execute("DELETE from productos")
cursor.execute("Select titulo from productos")
productos = cursor.fetchall()
print(productos)
conexion.commit()


#Insertar varios registros de golpe
productos = [
    ("Ordenar portatil", "Bupc", 200),
    (" portatil", "500 gb ram", 600),
    ("fuente poder", "fuente de 110 v", 500),
    ("silla", "silla de oficina", 100)
]

cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)
conexion.commit()

cursor.execute("Select * from productos")
print(cursor)
productos = cursor.fetchall()
print(productos)


# Cerrla conexi[on
conexion.close()