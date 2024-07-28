# Tema 1: Tipos de Variables en Python

Este es el primer tema del curso de Python. Aquí aprenderás sobre los tipos de variables, operadores lógicos y aritméticos, y cómo trabajar con strings y sus métodos.

## Contenido
1. [Tipos de Variables](./01_Tipos_de_Variables.py)
2. [Operadores Lógicos y Aritméticos](./02_Operadores_Lógicos_Aritméticos)
3. [Strings](./03_Strings.py)
4. [Métodos de los Strings](./04_Métodos_String.py)
5. [Conclusión](#conclusión)

## Tipos de Variables 📘

En Python, existen varios tipos de variables que puedes utilizar. Aquí hay una descripción de los tipos más comunes:

| Tipo    | Descripción                    | Ejemplo                         |
|---------|--------------------------------|---------------------------------|
| int     | Enteros                        | `x = 5`                         |
| float   | Números de punto flotante      | `y = 3.14`                      |
| str     | Cadenas de texto               | `name = "Python"`               |
| bool    | Valores booleanos              | `is_active = True`              |
| list    | Listas (mutables)              | `my_list = [1, 2, 3]`           |
| tuple   | Tuplas (inmutables)            | `my_tuple = (1, 2, 3)`          |
| dict    | Diccionarios                   | `my_dict = {"key": "value"}`    |

### Ejemplos

```python
# Entero
x = 10

# Flotante
y = 3.14

# Cadena de texto
name = "Python"

# Booleano
is_active = True

# Lista
my_list = [1, 2, 3, 4, 5]

# Tupla
my_tuple = (1, 2, 3, 4, 5)

# Diccionario
my_dict = {"name": "John", "age": 30}
```

## Operadores Lógicos y Aritméticos 📘

### Operadores Aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas:

| Operador | Descripción       | Ejemplo     |
|----------|-------------------|-------------|
| +        | Suma              | `a + b`     |
| -        | Resta             | `a - b`     |
| *        | Multiplicación    | `a * b`     |
| /        | División          | `a / b`     |
| %        | Módulo            | `a % b`     |
| **       | Exponenciación    | `a ** b`    |
| //       | División entera   | `a // b`    |

#### Ejemplos

```python
a = 10
b = 3

print(a + b)  # Suma: 13
print(a - b)  # Resta: 7
print(a * b)  # Multiplicación: 30
print(a / b)  # División: 3.3333...
print(a % b)  # Módulo: 1
print(a ** b) # Exponenciación: 1000
print(a // b) # División entera: 3
```

### Operadores Lógicos

Los operadores lógicos se utilizan para realizar operaciones lógicas:

| Operador | Descripción                                        |
|----------|----------------------------------------------------|
| and      | Retorna `True` si ambas condiciones son verdaderas |
| or       | Retorna `True` si una de las condiciones es verdadera |
| not      | Invierte el valor lógico                           |

#### Ejemplos

```python
x = True
y = False

print(x and y) # False
print(x or y)  # True
print(not x)   # False
```

## Strings 📘

Un string es una secuencia de caracteres. Puedes definir un string utilizando comillas simples (`'`) o dobles (`"`):

### Ejemplos

```python
# Comillas simples
single_quote_string = 'Hola, Mundo!'

# Comillas dobles
double_quote_string = "Hola, Mundo!"

# Triple comillas para strings multilínea
multi_line_string = """Este es un string
multilínea.
"""
```

## Métodos de los Strings 📘

Los strings en Python tienen muchos métodos útiles. Aquí algunos de los más comunes:

| Método    | Descripción                                               |
|-----------|-----------------------------------------------------------|
| len()     | Retorna la longitud del string                            |
| upper()   | Convierte el string a mayúsculas                          |
| lower()   | Convierte el string a minúsculas                          |
| strip()   | Elimina los espacios en blanco al inicio y al final del string |
| split()   | Divide el string en una lista                             |
| replace() | Reemplaza una subcadena por otra                          |

### Ejemplos

```python
text = " Hola, Mundo! "

# Longitud del string
print(len(text))  # 13

# Convertir a mayúsculas
print(text.upper())  # " HOLA, MUNDO! "

# Convertir a minúsculas
print(text.lower())  # " hola, mundo! "

# Eliminar espacios en blanco
print(text.strip())  # "Hola, Mundo!"

# Dividir el string en una lista
print(text.split())  # ['Hola,', 'Mundo!']

# Reemplazar una subcadena por otra
print(text.replace("Mundo", "Python"))  # " Hola, Python! "
```

## Conclusión

Este tema cubre los fundamentos de los tipos de variables, operadores lógicos y aritméticos, y la manipulación de strings en Python. Comprender estos conceptos es esencial para avanzar en el aprendizaje de Python y te proporcionará una base sólida para los temas más avanzados.

¡Gracias por leer el Tema 1 sobre Tipos de Variables en Python!
💜💜💜 HAPPY CODING 💜💜💜
