# Tema 4: Funciones en Python 🐍

Este es el cuarto tema del curso de Python. Aquí aprenderás sobre funciones, módulos, comprensión de listas y manejo de errores en Python.

## Contenido 📚🙌
1. [Funciones](./11_Funciones.py)
   - [Definición y llamada de funciones](#11-definición-y-llamada-de-funciones)
   - [Argumentos y parámetros](#12-argumentos-y-parámetros)
   - [Retorno de valores](#13-retorno-de-valores)
2. [Módulos](./12_Módulos.py)
   - [Importación de módulos](#21-importación-de-módulos)
   - [Creación de módulos](#22-creación-de-módulos)
3. [Comprensión de listas](./13_Compresión_de_Listas.py)
4. [Tipos de errores y manejo de excepciones](#4-tipos-de-errores-y-manejo-de-excepciones)
5. [Conclusión](#conclusión)

## 1. Funciones 📘

Las funciones son bloques de código reutilizables que realizan una tarea específica.

### 1.1 Definición y llamada de funciones

Para definir una función en Python, usamos la palabra clave `def`:

```python
def saludar():
    print("¡Hola, mundo!")

# Llamada a la función
saludar()
```

### 1.2 Argumentos y parámetros

Las funciones pueden aceptar argumentos y tener parámetros por defecto:

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Alice")  # Hola, Alice!
saludar("Bob", "Buenos días")  # Buenos días, Bob!
```

También podemos usar argumentos posicionales y de palabras clave:

```python
def describir_persona(nombre, edad, ciudad="Desconocida"):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

describir_persona("Carlos", 30)
describir_persona("Diana", 25, ciudad="Madrid")
```

### 1.3 Retorno de valores

Las funciones pueden devolver valores usando la palabra clave `return`:

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # 8
```

## 2. Módulos 📘

Los módulos son archivos que contienen definiciones y declaraciones de Python.

### 2.1 Importación de módulos

Puedes importar módulos completos o funciones específicas:

```python
# Importar un módulo completo
import math
print(math.pi)

# Importar funciones específicas
from random import randint
print(randint(1, 10))

# Importar con un alias
import datetime as dt
print(dt.datetime.now())
```

### 2.2 Creación de módulos

Puedes crear tus propios módulos. Por ejemplo, crea un archivo llamado `mi_modulo.py`:

```python
# mi_modulo.py
def saludar(nombre):
    return f"Hola, {nombre}!"

PI = 3.14159
```

Luego, puedes importarlo en otro archivo:

```python
import mi_modulo

print(mi_modulo.saludar("Alice"))
print(mi_modulo.PI)
```

## 3. Comprensión de listas 📘

La comprensión de listas es una forma concisa de crear listas en Python:

```python
# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Comprensión de lista con condición
pares = [x for x in range(20) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

También puedes usar comprensión de listas con diccionarios y conjuntos:

```python
# Comprensión de diccionario
cuadrados_dict = {x: x**2 for x in range(5)}
print(cuadrados_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Comprensión de conjunto
vocales_set = {letra for letra in "hello world" if letra in 'aeiou'}
print(vocales_set)  # {'e', 'o'}
```

## 4. Tipos de errores y manejo de excepciones

Python tiene varios tipos de errores incorporados y permite manejar excepciones.

Algunos tipos comunes de errores:
- `SyntaxError`: Error en la sintaxis del código
- `NameError`: Uso de una variable no definida
- `TypeError`: Operación en un tipo de dato incorrecto
- `ValueError`: Valor incorrecto para una operación
- `IndexError`: Índice fuera de rango en una secuencia
- `KeyError`: Clave no encontrada en un diccionario

Manejo de excepciones:

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Error: Debes introducir un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
else:
    print("La operación se realizó con éxito.")
finally:
    print("Fin del programa.")
```

## Conclusión

- Las **funciones** son bloques de código reutilizables que pueden aceptar argumentos y devolver valores.
- Los **módulos** permiten organizar y reutilizar código en diferentes archivos.
- La **comprensión de listas** ofrece una forma concisa y elegante de crear listas, diccionarios y conjuntos.
- El **manejo de excepciones** permite controlar y responder a errores de manera elegante.

Dominar estos conceptos te permitirá escribir código más organizado, eficiente y robusto en Python.
💜💜💜 HAPPY CODING 💜💜💜