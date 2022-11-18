
import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password  = password

    def registrar(self):
        #Cifrar contrasenia
        password_cifrado = hashlib.sha256()
        password_cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuario VALUES(null, %s, %s, %s, %s, %s)"
        fecha = datetime.datetime.now()

        data_usuario = (self.nombre, self.apellidos, self.email, password_cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql,data_usuario)
            database.commit()
        except Exception as e:
            print(f"----")

        database.close()
        return [cursor.rowcount, self]



    def identificar(self):
        # Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuario WHERE email = %s AND password = %s"

        # Cifrar contrasenia
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result




