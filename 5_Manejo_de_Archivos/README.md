# Tema 5: Manejo de Archivos en Python 🐍

Este es el sexto tema del curso de Python. Aquí aprenderás sobre cómo trabajar con archivos en Python, incluyendo cómo leer, escribir y manipular archivos.

## Contenido 📚🙌
1. [Apertura y Cierre de Archivos](#1-apertura-y-cierre-de-archivos)
2. [Lectura de Archivos](#2-lectura-de-archivos)
3. [Escritura en Archivos](#3-escritura-en-archivos)
4. [Manejo de Archivos con Contexto](#4-manejo-de-archivos-con-contexto)
5. [Trabajando con Rutas de Archivos](#5-trabajando-con-rutas-de-archivos)
6. [Manejo de Archivos CSV](#6-manejo-de-archivos-csv)
7. [Manejo de Archivos JSON](#7-manejo-de-archivos-json)
8. [Conclusión](#conclusión)

## 1. Apertura y Cierre de Archivos

Para trabajar con archivos en Python, primero necesitas abrirlos. La función `open()` se usa para esto.

```python
# Sintaxis básica
file = open('nombre_archivo.txt', 'modo')

# Modos comunes:
# 'r' - Lectura (por defecto)
# 'w' - Escritura (sobrescribe el archivo si existe)
# 'a' - Añadir (agrega al final del archivo)
# 'r+' - Lectura y escritura

# Siempre cierra el archivo después de usarlo
file.close()
```

## 2. Lectura de Archivos

Hay varias formas de leer el contenido de un archivo:

```python
# Leer todo el contenido
file = open('ejemplo.txt', 'r')
contenido = file.read()
print(contenido)
file.close()

# Leer línea por línea
file = open('ejemplo.txt', 'r')
for linea in file:
    print(linea)
file.close()

# Leer todas las líneas en una lista
file = open('ejemplo.txt', 'r')
lineas = file.readlines()
print(lineas)
file.close()
```

## 3. Escritura en Archivos

Para escribir en un archivo, usamos los modos 'w' o 'a':

```python
# Escribir en un archivo (sobrescribe el contenido existente)
file = open('nuevo_archivo.txt', 'w')
file.write('Hola, mundo!\n')
file.write('Esta es una nueva línea.')
file.close()

# Añadir al final de un archivo
file = open('nuevo_archivo.txt', 'a')
file.write('\nEsta línea se añade al final.')
file.close()
```

## 4. Manejo de Archivos con Contexto

La mejor práctica para trabajar con archivos es usar el manejo de contexto con `with`:

```python
# Lectura de archivo con manejo de contexto
with open('ejemplo.txt', 'r') as file:
    contenido = file.read()
    print(contenido)
# El archivo se cierra automáticamente al salir del bloque 'with'

# Escritura de archivo con manejo de contexto
with open('nuevo_archivo.txt', 'w') as file:
    file.write('Hola, mundo!\n')
    file.write('Esta es una nueva línea.')
```

## 5. Trabajando con Rutas de Archivos

El módulo `os.path` proporciona funciones para trabajar con rutas de archivos:

```python
import os.path

# Comprobar si un archivo existe
if os.path.exists('ejemplo.txt'):
    print('El archivo existe')

# Obtener el nombre del archivo de una ruta
nombre = os.path.basename('/ruta/al/archivo/ejemplo.txt')
print(nombre)  # ejemplo.txt

# Obtener el directorio de una ruta
directorio = os.path.dirname('/ruta/al/archivo/ejemplo.txt')
print(directorio)  # /ruta/al/archivo

# Unir rutas
ruta_completa = os.path.join('/ruta/al/archivo', 'ejemplo.txt')
print(ruta_completa)  # /ruta/al/archivo/ejemplo.txt
```

## 6. Manejo de Archivos CSV

Python proporciona el módulo `csv` para trabajar con archivos CSV:

```python
import csv

# Leer un archivo CSV
with open('datos.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Escribir en un archivo CSV
with open('nuevo_datos.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Nombre', 'Edad', 'Ciudad'])
    csv_writer.writerow(['Alice', '30', 'New York'])
    csv_writer.writerow(['Bob', '25', 'London'])
```

## 7. Manejo de Archivos JSON

Para trabajar con archivos JSON, Python proporciona el módulo `json`:

```python
import json

# Leer un archivo JSON
with open('datos.json', 'r') as file:
    data = json.load(file)
    print(data)

# Escribir en un archivo JSON
data = {
    'nombre': 'Alice',
    'edad': 30,
    'ciudad': 'New York'
}
with open('nuevo_datos.json', 'w') as file:
    json.dump(data, file, indent=4)
```

## Conclusión

El manejo de archivos es una habilidad crucial en Python:

- Permite leer y escribir datos persistentes.
- Es esencial para el procesamiento de datos y la automatización de tareas.
- Python proporciona herramientas robustas para trabajar con varios formatos de archivo, incluyendo texto plano, CSV y JSON.
- El uso del manejo de contexto (`with`) es la mejor práctica para trabajar con archivos de manera segura.
- Comprender cómo trabajar con rutas de archivos es importante para la portabilidad del código.

Dominar estas técnicas te permitirá crear programas más poderosos y útiles que pueden interactuar con datos almacenados en el sistema de archivos.
💜💜💜 HAPPY CODING 💜💜💜