### Módulos ###
## Un módulo es un archivo que contiene un conjunto de códigos o un conjunto de funciones 
# que se pueden incluir en una aplicación

## Creación de un módulo
# Para crear un módulo escribimos nuestros códigos en un script python y lo guardamos como un archivo .py
'mymodule.py file'

def generate_full_name(firstname, lastname):
      space = ' '
      fullname = firstname + space + lastname
      return fullname

def sum_two_nums (num1, num2):
    return num1 + num2
gravity = 9.81
person = {
    "firstname": "Marco",
    "age": 250,
    "country": "Roma",
    "city":'Grecia'
}

## Importación de un módulo
'main.py file'
'import "mymodule"'
print('mymodule'.generate_full_name('Marco', 'Aurelio')) 

# Podemos tener muchas funciones en un archivo y podemos importar todas las funciones de manera diferente
'main.py file'
'from mymodule import generate_full_name, sum_two_nums, person, gravity'
print(generate_full_name('Marco','Aurelio'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])

# Durante la importación podemos cambiar el nombre del módulo
'main.py file'
'from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g'
print('fullname'('Marco','Aurelio'))
print('total'(1, 9))
mass = 100;
weight = mass * 'g'
print(weight)
print('p')
print('p'['firstname'])

### Importar módulos integrados
## Algunos de los módulos integrados más comunes:
## math, datetime, os, sys, random, statistics, collections, json,re

## Módulo del sistema operativo
# Es posible realizar automáticamente muchas tareas del sistema operativo
'mport the module'
import os
# Creando un directorio
os.mkdir('directory_name')
# Cambiando el directorio actual
os.chdir('path')
# Obteniendo el directorio de trabajo actual
os.getcwd()
# Removiendo el directorio
os.rmdir()

## Módulo Sys
# Proporciona funciones y variables que se utilizan para manipular diferentes partes del entorno 
# de tiempo de ejecución de Python
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # Esta línea se imprimirá: filename argument1 argument2
print('Bienvenido {}. Disfruta  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# Ahora, para comprobar cómo funciona este script, escribí en la línea de comandos
'python script.py Asabeneh 30DaysOfPython'

# Algunos comandos sys útiles:
# Para salir del sistema
sys.exit()
# Para conocer la variable entera más grande que se necesita
sys.maxsize
# Para conocer la ruta del entorno
sys.path
# Para saber la versión de Python que estás usando
sys.version

## Módulo de estadísticas
# Proporciona funciones para la estadística matemática de datos numéricos
from statistics import * # importando todos los módulos de estadística
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

## Módulo de matemáticas
# Contiene muchas operaciones matemáticas y constantes
import math
print(math.pi)           # 3.141592653589793, constante pi
print(math.sqrt(2))      # 1.4142135623730951, raíz cuadrada
print(math.pow(2, 3))    # 8.0, función exponencial
print(math.floor(9.81))  # 9, redondeo para abajo
print(math.ceil(9.81))   # 10, redondeo para arriba
print(math.log10(100))   # 2, logaritmo de base 10

## Módulo aleatorio
# Nos da un número aleatorio entre 0 y 0,9999
from random import random, randint
print(random())   # si no le pasamos argumentos, retorna un valor entre 0 y 0,9999
print(randint(5, 20)) # retorna un valor aleatorio entre [5,20] inclusive