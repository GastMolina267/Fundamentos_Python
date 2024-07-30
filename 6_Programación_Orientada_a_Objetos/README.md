# Tema 6: Programación Orientada a Objetos (POO) en Python 🐍

Este tema cubre los conceptos fundamentales de la Programación Orientada a Objetos en Python, una paradigma de programación que organiza el diseño de software en torno a datos u objetos, en lugar de funciones y lógica.

## Contenido 📚🙌
1. [Introducción a la POO](#1-introducción-a-la-poo)
2. [Clases y Objetos](#2-clases-y-objetos)
3. [Atributos y Métodos](#3-atributos-y-métodos)
4. [Constructores y Destructores](#4-constructores-y-destructores)
5. [Encapsulación](#5-encapsulación)
6. [Herencia](#6-herencia)
7. [Polimorfismo](#7-polimorfismo)
8. [Métodos Especiales](#8-métodos-especiales)
9. [Decoradores de Clase](#9-decoradores-de-clase)
10. [Conclusión](#conclusión)

## 1. Introducción a la POO

La Programación Orientada a Objetos es un paradigma de programación basado en el concepto de "objetos", que pueden contener datos y código. Los datos están en forma de campos (a menudo conocidos como atributos), y el código está en forma de procedimientos (a menudo conocidos como métodos).

Conceptos clave de la POO:
- Clases y Objetos
- Encapsulación
- Herencia
- Polimorfismo

## 2. Clases y Objetos

Una clase es un plano para crear objetos. Un objeto es una instancia de una clase.

```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Creando un objeto de la clase Perro
mi_perro = Perro("Fido", 3)
mi_perro.ladrar()  # Salida: Fido dice: ¡Guau!
```

## 3. Atributos y Métodos

Los atributos son variables que pertenecen a una clase. Los métodos son funciones que pertenecen a una clase.

```python
class Circulo:
    pi = 3.14159  # Atributo de clase

    def __init__(self, radio):
        self.radio = radio  # Atributo de instancia

    def area(self):  # Método
        return self.pi * self.radio ** 2

circulo = Circulo(5)
print(f"Área del círculo: {circulo.area()}")
```

## 4. Constructores y Destructores

El constructor `__init__` se llama cuando se crea un objeto. El destructor `__del__` se llama cuando se destruye un objeto.

```python
class Persona:
    def __init__(self, nombre):
        print(f"Se ha creado a {nombre}")
        self.nombre = nombre

    def __del__(self):
        print(f"{self.nombre} ha sido eliminado")

persona = Persona("Alice")
del persona  # Elimina explícitamente el objeto
```

## 5. Encapsulación

La encapsulación es el empaquetamiento de datos y métodos que operan en esos datos dentro de una sola unidad (clase). En Python, usamos convenciones de nomenclatura para indicar el nivel de acceso.

```python
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo())  # 1500
```

## 6. Herencia

La herencia permite que una clase herede atributos y métodos de otra clase.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"

perro = Perro("Fido")
gato = Gato("Whiskers")

print(perro.hablar())  # Fido dice: ¡Guau!
print(gato.hablar())   # Whiskers dice: ¡Miau!
```

## 7. Polimorfismo

El polimorfismo permite que objetos de diferentes clases sean tratados como objetos de una clase común.

```python
def hacer_hablar(animal):
    print(animal.hablar())

perro = Perro("Fido")
gato = Gato("Whiskers")

hacer_hablar(perro)  # Fido dice: ¡Guau!
hacer_hablar(gato)   # Whiskers dice: ¡Miau!
```

## 8. Métodos Especiales

Python tiene métodos especiales (también conocidos como métodos dunder) que permiten definir el comportamiento de las clases en situaciones específicas.

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

    def __eq__(self, otro):
        if isinstance(otro, Libro):
            return self.titulo == otro.titulo and self.autor == otro.autor
        return False

libro1 = Libro("1984", "George Orwell")
libro2 = Libro("1984", "George Orwell")

print(libro1)  # 1984 por George Orwell
print(libro1 == libro2)  # True
```

## 9. Decoradores de Clase

Los decoradores de clase permiten modificar o extender el comportamiento de las clases.

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class ConfiguracionDB:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432

config1 = ConfiguracionDB()
config2 = ConfiguracionDB()
print(config1 is config2)  # True
```

## Conclusión

La Programación Orientada a Objetos en Python proporciona una forma poderosa y flexible de estructurar y organizar el código:

- Las **clases y objetos** permiten crear estructuras de datos complejas y reutilizables.
- La **encapsulación** ayuda a ocultar los detalles internos y proteger la integridad de los datos.
- La **herencia** facilita la creación de jerarquías de clases y la reutilización de código.
- El **polimorfismo** permite escribir código más flexible y extensible.
- Los **métodos especiales** proporcionan una forma de personalizar el comportamiento de las clases.
- Los **decoradores de clase** ofrecen una manera elegante de modificar clases.

Dominar estos conceptos de POO te permitirá diseñar y implementar sistemas de software más robustos, mantenibles y escalables en Python.
💜💜💜 HAPPY CODING 💜💜💜