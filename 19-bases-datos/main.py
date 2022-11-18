import mysql.connector

#conexión
database = mysql.connector.connect(
     host="192.168.18.9",
     user="root",
     passwd="root",
 )

# La conexión ha sido correcta?
# print(database)
cursor = database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute("SHOW DATABASES")

#Imprimo o muestro las bases de datos existentes
for bd in cursor:
    print(bd)

#Cierro la conexión
database.close()

print("--------------------")
# conexión nuevamente ya a una base de datos específica
database = mysql.connector.connect(
    host="192.168.18.9",
    user="root",
    passwd="root",
    database = 'master_python'
)
cursor = database.cursor(buffered=True)

cursor.execute("""
CREATE TABLE IF NOT EXISTS VEHICULOS (ID INT(10) AUTO_INCREMENT NOT NULL,
MARCA VARCHAR(40) NOT NULL,
MODELO VARCHAR(40) NOT NULL,
PRECIO FLOAT(10,2) NOT NULL,
CONSTRAINT PK_VEHICULO PRIMARY KEY(ID)
)
""")

cursor.execute("SHOW TABLES")
#mostrando las tablas creadas
for table in cursor:
     print(table)

### - Se ha documentado para que no siga ingresando
##Insertando un registro
#cursor.execute("INSERT INTO VEHICULOS VALUES(null, 'Open', 'Astra', 18500)")
#database.commit()

cursor.execute("SELECT * from VEHICULOS")
#Imprimiendo los registros existentes en la base de datos
for registro in cursor:
     print(registro)

#Insertando datos de manera masiva
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Hyundai', 'Tucson', 15000),
    ('Chevrolet', 'Aveo', 8000)
]

### - Se ha documentado para que no siga ingresando
#cursor.executemany("INSERT INTO VEHICULOS VALUES(NULL, %s,%s,%s)", coches)
database.commit()

cursor.execute("SELECT * from VEHICULOS")
#Imprimiendo los registros existentes en la base de datos
for registro in cursor:
     print(registro)


#Recuperando todos los coches en una lista
print("Todos los autos cuyos costos mayor a $5001")
cursor.execute("SELECT * from VEHICULOS WHERE precio >= 5001")
result = cursor.fetchall()
for autos in result:
     print(autos[1], autos[3])


#Obteniendo unicamente la primera fila de la tabla
cursor.execute("SELECT * from VEHICULOS WHERE precio >= 5001")
resultado_primero = cursor.fetchone()
print(resultado_primero)

#Borrando registros
cursor.execute("DELETE FROM VEHICULOS WHERE MARCA = 'Open'")
database.commit()

print("Despues de borrar")
#Consultando nuevamente los vehiculos
cursor.execute("SELECT * from VEHICULOS")
result = cursor.fetchall()
print(result)
for autos in result:
     print(autos[1], autos[3])


#Actualizando
print("Actualizando")
cursor.execute("UPDATE VEHICULOS SET modelo = 'CAMBIADO' WHERE marca = 'Chevrolet'")
database.commit()

#Consultando nuevamente los vehiculos
cursor.execute("SELECT * from VEHICULOS")
result = cursor.fetchall()
print(result)
for autos in result:
     print(autos[1], autos[2])




