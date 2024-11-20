import mysql.connector
from mysql.connector import Error

# Función para establecer la conexión con la base de datos MySQL
def crear_conexion():
    print("Intentando conectar a la base de datos...")  # Mensaje de inicio de la conexión
    try:
        # Intentamos establecer una conexión con la base de datos utilizando los parámetros especificados
        conexion = mysql.connector.connect(
            host='localhost',          # Dirección del servidor MySQL (en este caso, localhost para conexión local)
            user='root',               # Usuario de MySQL con privilegios suficientes para acceder a la base de datos
            password='campusfp',       # Contraseña del usuario de MySQL
            database='encuestas',      # Nombre de la base de datos a la que nos conectamos
            auth_plugin='mysql_native_password'  # Mecanismo de autenticación utilizado en MySQL
        )
        
        # Verificamos si la conexión fue exitosa
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")  # Si la conexión es exitosa, se informa al usuario
            return conexion  # Devolvemos el objeto de conexión para poder utilizarlo en otras partes del código
    except Error as err:
        # Si ocurre algún error durante la conexión, se captura y muestra el error
        print(f"Error de conexión a la base de datos: {err}")
        return None  # Si la conexión falla, devolvemos None

# Función para cerrar la conexión con la base de datos
def cerrar_conexion(conexion):
    try:
        # Verificamos si la conexión está activa antes de intentar cerrarla
        if conexion and conexion.is_connected():
            conexion.close()  # Cerramos la conexión
            print("Conexión cerrada correctamente.")  # Confirmamos que la conexión se cerró con éxito
    except Error as err:
        # Si ocurre un error al cerrar la conexión, lo capturamos y mostramos
        print(f"Error al cerrar la conexión: {err}")
