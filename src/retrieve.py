from src.conectionLayer import conexion, cursor

# Librería para manipulación de imágenes
from PIL import Image
import io



# Insercción de imágenes en la base de datos
def buscar_imagen():

    int(input("Introduce el ID del trabajador"))
    cursor.execute("SELECT imagen from trabajadores where id = %s", (id))
    registro = cursor.fetchone()
    imagen = registro[0]
    convertir_blob_imagen(imagen).show()
    conexion.close()


# Conversión de blob a archivo de imagen legible
def convertir_blob_imagen(imagen):
    bytes_imagen = io.BytesIO(imagen)
    archivo_imagen = Image.open(bytes_imagen)
    
    return archivo_imagen