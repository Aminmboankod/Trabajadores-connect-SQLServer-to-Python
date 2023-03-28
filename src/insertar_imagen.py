from src.db.acceso_bd import cursor, conexion
import base64
import os


ruta = "../src/imagen/"
fotos = sorted(os.listdir(ruta))



def insertar():
    for imagen in fotos:

        # Leer la imagen que deseas insertar en modo binario
        with open(ruta + str(imagen), 'rb') as archivo_imagen:
            datos_imagen = archivo_imagen.read()

        # Convertir la imagen en datos binarios
        datos_binarios = base64.b64encode(datos_imagen)

        # Ejecutar la consulta SQL para insertar la imagen en la tabla
        consulta = "INSERT INTO Trabajador (Foto) VALUES (?)"
        cursor.execute(consulta, datos_binarios)
        conexion.commit()

        # Cerrar la conexión a la base de datos
        conexion.close()