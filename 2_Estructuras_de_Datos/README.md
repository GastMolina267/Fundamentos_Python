# Tema 2: Estructuras de Datos en Python

Este es el segundo tema del curso de Python. Aquí aprenderás sobre las principales estructuras de datos en Python: listas, tuplas, conjuntos (sets) y diccionarios.

## Contenido
1. [Listas](./05_Listas.py)
2. [Tuplas](./06_Tuplas.py)
3. [Conjuntos (Sets)](./07_Sets_Conjunto.py)
4. [Diccionarios](./08_Diccionarios.py)
5. [Conclusión](#conclusión)

## 1. Listas

Las listas son estructuras de datos mutables y ordenadas que pueden contener elementos de diferentes tipos.

### Características principales:
- Mutables (se pueden modificar después de su creación)
- Ordenadas (mantienen el orden de inserción)
- Permiten duplicados
- Se definen con corchetes `[]`

### Ejemplos:

```python
# Crear una lista
frutas = ["manzana", "banana", "cereza"]

# Acceder a elementos
print(frutas[0])  # manzana

# Modificar elementos
frutas[1] = "pera"

# Añadir elementos
frutas.append("uva")

# Eliminar elementos
frutas.remove("cereza")

# Longitud de la lista
print(len(frutas))  # 3

# Iterar sobre una lista
for fruta in frutas:
    print(fruta)
```

## 2. Tuplas

Las tuplas son estructuras de datos inmutables y ordenadas.

### Características principales:
- Inmutables (no se pueden modificar después de su creación)
- Ordenadas
- Permiten duplicados
- Se definen con paréntesis `()`

### Ejemplos:

```python
# Crear una tupla
coordenadas = (10, 20)

# Acceder a elementos
print(coordenadas[0])  # 10

# No se pueden modificar elementos
# Esto lanzaría un error: coordenadas[0] = 15

# Desempaquetar una tupla
x, y = coordenadas

# Longitud de la tupla
print(len(coordenadas))  # 2

# Iterar sobre una tupla
for coord in coordenadas:
    print(coord)
```

## 3. Conjuntos (Sets)

Los conjuntos son colecciones no ordenadas de elementos únicos.

### Características principales:
- Mutables (el conjunto en sí, no sus elementos)
- No ordenados
- No permiten duplicados
- Se definen con llaves `{}` o la función `set()`

### Ejemplos:

```python
# Crear un conjunto
colores = {"rojo", "verde", "azul"}

# Añadir elementos
colores.add("amarillo")

# Eliminar elementos
colores.remove("verde")

# Operaciones de conjunto
otros_colores = {"azul", "amarillo", "naranja"}
print(colores.union(otros_colores))
print(colores.intersection(otros_colores))

# Comprobar pertenencia
print("rojo" in colores)  # True

# Longitud del conjunto
print(len(colores))  # 3
```

## 4. Diccionarios

Los diccionarios son estructuras de datos que almacenan pares clave-valor.

### Características principales:
- Mutables
- No ordenados (en versiones de Python < 3.7)
- Las claves deben ser únicas e inmutables
- Se definen con llaves `{}` y dos puntos `:` para separar clave y valor

### Ejemplos:

```python
# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a valores
print(persona["nombre"])  # Juan

# Modificar valores
persona["edad"] = 31

# Añadir nuevos pares clave-valor
persona["profesion"] = "Ingeniero"

# Eliminar pares clave-valor
del persona["ciudad"]

# Obtener todas las claves y valores
print(persona.keys())
print(persona.values())

# Iterar sobre un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Longitud del diccionario
print(len(persona))  # 3
```

## Conclusión

Las estructuras de datos en Python (listas, tuplas, conjuntos y diccionarios) son fundamentales para organizar y manipular datos de manera eficiente. Cada una tiene sus propias características y casos de uso:

- Usa **listas** cuando necesites una colección ordenada y mutable de elementos.
- Usa **tuplas** para colecciones ordenadas e inmutables, como coordenadas o datos que no deben cambiar.
- Usa **conjuntos** cuando necesites almacenar elementos únicos y realizar operaciones de conjunto.
- Usa **diccionarios** para almacenar pares clave-valor y acceder rápidamente a valores por su clave.

Dominar estas estructuras de datos te permitirá escribir código más eficiente y elegante en Python.
💜💜💜 HAPPY CODING 💜💜💜