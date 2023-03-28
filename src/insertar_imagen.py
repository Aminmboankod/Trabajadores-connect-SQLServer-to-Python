from src.db.acceso_bd import cursor, conexion
import base64
import os


ruta = "../src/imagen/"
fotos = sorted(os.listdir(ruta))
id = 1


def insertar():
    for imagen in fotos:

        # Leer la imagen que deseas insertar en modo binario
        with open(ruta + str(imagen), 'rb') as archivo_imagen:

            datos_imagen = archivo_imagen.read()

            # Convertir la imagen en datos binarios
            datos_binarios = base64.b64encode(datos_imagen)

            # Ejecutar la consulta SQL para insertar la imagen en la tabla
            consulta = "UPDATE Trabajador SET Foto = %s WHERE ID = %s"
            cursor.execute(consulta, (datos_binarios, id))
            conexion.commit()

            # Cerrar la conexión a la base de datos
            conexion.close()

            id += 1


def insertar_trabajador():

    id_trabajador = input("Inserta el ID del trabajador al que quieras añadirle una imagen: ")
    foto_trabajador = input("Inserta la imagen que quieres añadir al trabajador")
    with open(ruta + foto_trabajador, 'rb') as archivo_imagen:

        datos_imagen = archivo_imagen.read()
        datos_binarios = base64.b16decode(datos_imagen)
        consulta = "UPDATE Trabajador SET Foto = %s WHERE ID = %s"
        cursor.execute(consulta, (datos_binarios, id_trabajador))
        conexion.commit()
        conexion.close()