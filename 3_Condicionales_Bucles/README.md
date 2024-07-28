# Tema 3: Condicionales y Bucles en Python 🐍

Este es el tercer tema del curso de Python. Aquí aprenderás sobre las estructuras de control de flujo en Python: condicionales y bucles.

## Contenido 📚🙌
1. [Condicionales](./09_Condicionales.py)
   - [if, elif, else](#11-if-elif-else)
   - [Operadores de comparación](#12-operadores-de-comparación)
   - [Operadores lógicos](#13-operadores-lógicos)
2. [Bucles](./10_Bucles.py)
   - [for](#21-for)
   - [while](#22-while)
   - [break, continue y pass](#23-break-continue-y-pass)
3. [Conclusión](#conclusión)

## 1. Condicionales 📘

Las estructuras condicionales permiten ejecutar diferentes bloques de código basándose en ciertas condiciones.

### 1.1 if, elif, else

La estructura básica de un condicional en Python es:

```python
if condicion:
    # código si la condición es verdadera
elif otra_condicion:
    # código si la otra condición es verdadera
else:
    # código si ninguna de las condiciones anteriores es verdadera
```

Ejemplo:

```python
edad = 18

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Acabas de alcanzar la mayoría de edad")
else:
    print("Eres mayor de edad")
```

### 1.2 Operadores de comparación

Los operadores de comparación se utilizan en las condiciones:

- `==`: Igual a
- `!=`: No igual a
- `<`: Menor que
- `>`: Mayor que
- `<=`: Menor o igual que
- `>=`: Mayor o igual que

Ejemplo:

```python
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False
```

### 1.3 Operadores lógicos

Los operadores lógicos se utilizan para combinar condiciones:

- `and`: Verdadero si ambas condiciones son verdaderas
- `or`: Verdadero si al menos una condición es verdadera
- `not`: Invierte el valor de la condición

Ejemplo:

```python
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad >= 18 or tiene_licencia:
    print("Cumples al menos uno de los requisitos para conducir")
else:
    print("No puedes conducir")

if not tiene_licencia:
    print("Necesitas obtener una licencia")
```

## 2. Bucles 📘

Los bucles permiten ejecutar un bloque de código repetidamente.

### 2.1 for

El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena).

Sintaxis básica:

```python
for elemento in secuencia:
    # código a ejecutar para cada elemento
```

Ejemplos:

```python
# Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Iterar sobre un rango de números
for i in range(5):
    print(i)  # Imprime números del 0 al 4

# Iterar sobre un diccionario
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

### 2.2 while

El bucle `while` se ejecuta mientras una condición sea verdadera.

Sintaxis básica:

```python
while condicion:
    # código a ejecutar mientras la condición sea verdadera
```

Ejemplo:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### 2.3 break, continue y pass

- `break`: Termina el bucle actual
- `continue`: Salta a la siguiente iteración del bucle
- `pass`: No hace nada, se usa como marcador de posición

Ejemplos:

```python
# break
for i in range(10):
    if i == 5:
        break
    print(i)  # Imprime números del 0 al 4

# continue
for i in range(5):
    if i == 2:
        continue
    print(i)  # Imprime 0, 1, 3, 4

# pass
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)  # Imprime 0, 1, 3, 4
```

## Conclusión

Los condicionales y bucles son fundamentales en la programación Python:

- Los **condicionales** (`if`, `elif`, `else`) permiten ejecutar código basado en condiciones específicas.
- Los **bucles** (`for`, `while`) permiten repetir código de manera eficiente.
- Los operadores de comparación y lógicos son esenciales para construir condiciones complejas.
- `break`, `continue` y `pass` ofrecen control adicional sobre el flujo de ejecución en los bucles.

Dominar estas estructuras de control te permitirá crear programas más complejos y eficientes en Python.
💜💜💜 HAPPY CODING 💜💜💜