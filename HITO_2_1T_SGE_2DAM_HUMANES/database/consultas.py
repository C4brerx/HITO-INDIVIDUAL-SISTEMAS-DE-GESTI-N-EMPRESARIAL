from binascii import Error
from database.conexion import crear_conexion, cerrar_conexion

# Obtiene todas las encuestas de la base de datos, ordenadas según el parámetro 'orden' (por defecto por 'edad')
def obtener_encuestas(orden="edad"):
    conexion = crear_conexion() 
    if not conexion: 
        return []
    try:
        cursor = conexion.cursor() 
        # Ejecutamos la consulta SQL para obtener todas las encuestas ordenadas por el campo 'orden'
        cursor.execute(f"SELECT * FROM encuesta ORDER BY {orden}")
        resultados = cursor.fetchall()  # Obtenemos todos los resultados de la consulta
        return resultados  
    except Exception as e:  
        print(f"Error al obtener encuestas: {e}")
        return []  
    finally:
        cerrar_conexion(conexion)

# Actualiza los datos de una encuesta específica
def actualizar_encuesta(edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, 
                        bebidas_destiladas_semana, vinos_semana, perdidas_control, 
                        diversion_dependencia_alcohol, problemas_digestivos, tension_alta, 
                        dolor_cabeza):
    conexion = crear_conexion()  # Establecemos la conexión a la base de datos
    if not conexion: 
        return
    try:
        cursor = conexion.cursor()  # Creamos un cursor para ejecutar la consulta SQL
        sql = '''  # Definimos la consulta SQL para actualizar una encuesta
            UPDATE encuesta
            SET edad=%s, sexo=%s, bebidas_semana=%s, cervezas_semana=%s, bebidas_fin_semana=%s,
                bebidas_destiladas_semana=%s, vinos_semana=%s, perdidas_control=%s,
                diversion_dependencia_alcohol=%s, problemas_digestivos=%s, 
                tension_alta=%s, dolor_cabeza=%s
            WHERE id=%s
        '''
        # Definimos los valores que se usarán en la consulta SQL
        datos = (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                 bebidas_destiladas_semana, vinos_semana, perdidas_control, 
                 diversion_dependencia_alcohol, problemas_digestivos, 
                 tension_alta, dolor_cabeza)
        cursor.execute(sql, datos)  
        conexion.commit()  
        print("Encuesta actualizada correctamente")  # Mensaje de éxito
    except Exception as e:  
        print(f"Error al actualizar encuesta: {e}")
    finally:
        cerrar_conexion(conexion) 

# Inserta una nueva encuesta en la base de datos
def insertar_encuesta(conn, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                      bebidas_destiladas_semana, vinos_semana, perdidas_control, 
                      diversion_dependencia_alcohol, problemas_digestivos, 
                      tension_alta, dolor_cabeza):
    try:
        cursor = conn.cursor() 
        query = """  # Definimos la consulta SQL para insertar una nueva encuesta
        INSERT INTO encuesta (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, 
                               bebidas_destiladas_semana, vinos_semana, perdidas_control, 
                               diversion_dependencia_alcohol, problemas_digestivos, 
                               tension_alta, dolor_cabeza)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        values = (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                  bebidas_destiladas_semana, vinos_semana, perdidas_control, 
                  diversion_dependencia_alcohol, problemas_digestivos, 
                  tension_alta, dolor_cabeza)
        cursor.execute(query, values)  # Ejecutamos la consulta con los valores
        conn.commit() 
        print("Encuesta insertada correctamente")  # Mensaje de éxito
    except Error as e:  # Capturamos cualquier error que ocurra durante la inserción
        print(f"Error al insertar encuesta: {e}")
        conn.rollback()  # Si ocurre un error, deshacemos la operación para evitar dejar la base de datos en un estado inconsistente
    finally:
        cursor.close()  
# Elimina una encuesta de la base de datos por su ID
def eliminar_encuesta(id_encuesta):
    conexion = crear_conexion()  
    if not conexion:  
        return
    try:
        cursor = conexion.cursor()  # Creamos un cursor para ejecutar la consulta SQL
        sql = "DELETE FROM encuesta WHERE id = %s"  
        cursor.execute(sql, (id_encuesta,))  
        conexion.commit()  
        print("Encuesta eliminada correctamente")  
    except Exception as e:  
        print(f"Error al eliminar encuesta: {e}")
    finally:
        cerrar_conexion(conexion)  # Cerramos la conexión a la base de datos
