import mysql.connector



# Variable donde se encuentra el contexto de la conexión a la base de datos
try:
    conexion = mysql.connector(host='localhost',
                               database='Trabajadores',
                               user='root',
                               password='')

    # Objeto cursor para manipular los resultados de las consultas a la base de datos. 
    # Pêrmite enviar consultas y recibir los resultados.
    cursor = conexion.cursor()

except mysql.connector.Error as e:
    print("Error al conectar a la base de datos:", e)




