# Proyecto conexión a base de datos

En este repositorio encontraras la presentación de un proyecto que presentamos Adrián López y Amin Mustafa para la asignatura de primero del grado Superior de Desarrollo de aplicaciones Web Bases de datos. 


# Introducción


Este proyecto tiene como objetivo combinar los diferentes conceptos aprendidos durante la unidad de trabajo de SQL.
Entre los conceptos a incluir se encuentran las restricciones de integridad, integridad referencial, acciones en cascada en integridad referencial, tipos de datos de fecha, hora o marca de tiempo, grandes objetos binarios, dominios, índices, usuarios, privilegios y roles.
Se busca crear una base de datos que tenga un diseño adecuado y eficiente, con tablas que incluyan las restricciones de integridad necesarias para garantizar la integridad de los datos. Además, se deben incluir tablas que hagan uso de la integridad referencial y las acciones en cascada para mantener la consistencia de los datos.
Se utilizarán diferentes tipos de datos, incluyendo aquellos relacionados con fechas, horas y marcas de tiempo, así como los grandes objetos binarios.
Se crearán dominios que faciliten el manejo de los datos y se utilizarán índices para mejorar el rendimiento de las consultas.
También se debe incluir la creación de usuarios y la asignación de privilegios y roles para garantizar la seguridad de la información en la base de datos.
En resumen, este proyecto busca aplicar los conocimientos adquiridos en la unidad de trabajo de SQL para crear una base de datos eficiente y segura que cumpla con los requisitos de integridad y consistencia de los datos.
Para realizar el mismo se utilizará SQL Server para poner en práctica los conocimientos adquiridos en la empresa y además poder investigar sobre usos de la tecnología para poderla usar en el centro de trabajo.


# Requisitos

✅ Restricciones de integridad
Se deben incluir las restricciones de integridad necesarias para garantizar la integridad de los datos en la base de datos. Estas restricciones pueden incluir restricciones de clave primaria, restricciones de clave foránea, restricciones de verificación y restricciones de unicidad.
✅ Integridad referencial y acciones en cascada
Se deben incluir tablas que hagan uso de la integridad referencial y las acciones en cascada para mantener la consistencia de los datos. Esto se puede lograr mediante el uso de restricciones de clave foránea y la especificación de acciones en cascada como "ON DELETE CASCADE" o "ON UPDATE CASCADE".
✅ Tipos de datos de fecha, hora o marca de tiempo
Se deben utilizar diferentes tipos de datos para manejar la información relacionada con fechas, horas y marcas de tiempo. Esto puede incluir tipos de datos como "DATE", "TIME", "DATETIME", "TIMESTAMP" y otros.

✅ Grandes objetos binarios
Se deben incluir tablas que contengan grandes objetos binarios, como imágenes, videos y archivos de audio. Estos objetos pueden ser almacenados como datos binarios en la base de datos y recuperados cuando sea necesario.

## Dominios e índices
Se deben crear dominios que faciliten el manejo de los datos en la base de datos. Además, se deben utilizar índices para mejorar el rendimiento de las consultas y acelerar la recuperación de datos.

## Usuarios, privilegios y roles
Se debe incluir la creación de usuarios y la asignación de privilegios y roles para garantizar la seguridad de la información en la base de datos. Los usuarios deben tener permisos limitados y solo se les debe dar acceso a la información necesaria para realizar sus tareas.


- [Indice](#)
   - [Instalación](#instalación)
   - [Uso](#uso)
   - [Dependencias](#dependencias)
      - [Docker]()

# Instalación

Para comenzar con el proceso de instalación y creación de la base de datos propuesta, vamos a enumerar e instalar todas las dependencias necesarias.

```
Docker 23.0.1
SQL Server 2022-RTM-CU2-ubuntu-20.04 (Imagen de Docker)
SQL Server Management Studio 19.0.2
```
Descarga y puesta en marcha del contenido del repositorio:
```
clone
pip3 install -r requirements.txt
```