### Archivos ###
## El manejo de archivos es una parte de importación de la programación 
# que nos permite crear, leer, actualizar y eliminar archivos.

## En Python, para manejar los datos, usamos la función incorporada open()
open('filename', 'mode') # mode(r, a, w, x, t,b) 

'''
- "r" - Lectura - Valor predeterminado. Abre un archivo para su lectura, devuelve un error si el archivo no existe
- "a" - Anexar - Abre un archivo para anexar, crea el archivo si no existe
- "w" - Write - Abre un archivo para escribir, crea el archivo si no existe
- "x" - Crear - Crea el archivo especificado, devuelve un error si el archivo existe
- "t" - Texto - Valor predeterminado. Modo de texto
- "b" - Binario - Modo binario (por ejemplo, imágenes)
'''

## Abrir archivos para leerlos
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

'El archivo abierto tiene diferentes métodos de lectura:read(),readline(), readlines()'

## read()
# Lee todo el texto como cadena
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

'En lugar de imprimir todo el texto, imprimamos los primeros 10 caracteres del archivo de texto'

f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

## readline()
# Lee solo la primera línea
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

## splitlines()
# Otra forma de obtener todas las líneas como una lista
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

## Abrir archivos para escribir y actualizar
'''
Para escribir en un fichero existente, debemos añadir un modo como parámetro a la función open():

- "a" - append - se agregará al final del archivo, si el archivo no lo hace, crea un nuevo archivo.
- "w" - write - sobrescribirá cualquier contenido existente, si el archivo no existe, lo crea.
'''

# Vamos a añadir un texto al archivo que hemos estado leyendo
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

# El siguiente método crea un nuevo archivo, si el archivo no existe
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

## Eliminación de archivos
'''
Hemos visto en la sección anterior, cómo crear y eliminar un directorio usando el módulo os. 
De nuevo ahora, si queremos eliminar un archivo, usamos el módulo os
'''
import os
os.remove('./files/example.txt')

# Si el archivo no existe, el método remove generará un error
# por lo que es bueno usar una condición como esta:
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')