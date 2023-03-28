import pyodbc

# Variables que tienes que configurar según los 
# datos de acceso a la base de datos que hayas creado
server = 'Localhost,1433' 
database = 'Trabajadores' 
username = 'sa' 
password = '1234567890' 

# Variable donde se encuentra el contexto de la conexión a la base de datos
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

    # Objeto cursor para manipular los resultados de las consultas a la base de datos. 
    # Pêrmite enviar consultas y recibir los resultados.
    cursor = conexion.cursor()

except pyodbc.Error as e:
    print("Error al conectar a la base de datos:", e)




