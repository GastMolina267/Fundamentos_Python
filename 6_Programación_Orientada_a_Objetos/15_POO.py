### POO ###
## Una clase es como un constructor de objetos, o un "modelo" para crear objetos

## Creación de una clase
'''
Para crear una clase necesitamos la palabra clave "class"seguida del nombre y los dos puntos. 
El nombre de la clase debe ser CamelCase.
'''
class ClassName:
  'code goes here'

class Person:
  pass
print(Person)

## Creación de un Objeto
p = Person()
print(p)

## Constructor de una Clase
'''
La función constructora init tiene un parámetro self, 
que es una referencia a la instancia actual de la clase
'''
class Person:
      def __init__ (self, name):
          self.name =name

p = Person('Marco')
print(p.name)
print(p)

# Agreguemos más parámetros a la función constructora
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Marco', 'Aurelio', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

## Métodos de Objetos
'''
Los objetos pueden tener métodos. 
Los métodos son funciones que pertenecen al objeto.
'''
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} tiene {self.age} años de edad. El vive en {self.city}, {self.country}'

p = Person('Marco', 'Aurelio', 250, 'Finland', 'Helsinki')
print(p.person_info())

## Métodos predeterminados de objetos
'''
Si damos valores predeterminados para los parámetros en el constructor, 
podemos evitar errores cuando llamamos o instanciamos nuestra clase sin parámetros
'''
class Person:
      def __init__(self, firstname='Marco', lastname='Aurelio', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} tiene {self.age} años de edad. El vive en {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

## Método para modificar los valores predeterminados de la clase
'''
En el ejemplo siguiente, la clase person, todos los parámetros del constructor tienen valores predeterminados. 
Además de eso, tenemos el parámetro skills, al que podemos acceder mediante un método.
'''
class Person:
      def __init__(self, firstname='Marco', lastname='Aurelio', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} tiene {self.age} años de edad. El vive en {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

## Encapsulamiento
'''
Permite restringir el acceso a ciertos componentes del objeto, protegiendo los datos y asegurando que se manipulen de manera controlada
'''
# Atributos Públicos
'Accesibles desde cualquier parte del programa'
class Person:
      def __init__(self, firstname='Marco', lastname='Aurelio', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname # <--- Para que sea público, no se le agrega nada al atributo
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
p1 = Person()
print(p1.firstname) # Output: Marco

# Atributos Privados
'Sólo son accesibles dentro de la propia clase'
class Person:
      def __init__(self, firstname='Marco', lastname='Aurelio', age=250, country='Finland', city='Helsinki'):
          self.__firstname = firstname # <--- Para que sea privado, se le agrega __ al atributo
          self.__lastname = lastname
          self.__age = age
          self.__country = country
          self.__city = city

p2 = Person()
print(p2.__firstname) # Output: Error

## Acceso a los atributos privados. Métodos Getter y Setter
class Player:
    def __init__(self, name, ability, level, health, mana):
        self.__name = name
        self.__ability = ability
        self.__level = level
        self.__health = health
        self.__mana = mana
# Getter
'''
Un método que permite acceder a un atributo privado desde fuera de la clase
Se utiliza para obtener el valor de un atributo privado de manera controlada
'''
def get_name(self):
    return self.__name

def get_ability(self):
    return self.__ability

def get_level(self):
    return self.__level

def get_health(self):
    return self.__health

def get_mana(self):
    return self.__mana
# Setter
'''
Un método que permite modificar un atributo privado desde fuera de la clase
Se utiliza para establecer o cambiar el valor de un atributo privado de manera controlada
'''
def set_level(self, new_level):
    self.__level = new_level

p3 = Player("Marco","philosopher", 50, 100, 0)
print(p3.get_name)
print(p3.set_level(102))

## Herencia
'''
Permite crear una nueva clase a partir de una clase existente.
La nueva clase, llamada clase derivada o subclase, hereda los atributos y métodos de la clase base o superclase
Permite reutilizar el código de una clase ya existente
'''
class Player: # <--- Clase Base 
    def __init__(self, name, ability, level, health, mana):
        self.__name = name
        self.__ability = ability
        self.__level = level
        self.__health = health
        self.__mana = mana

class Magician(Player): # <--- Clase Heredada
    def __init__(self, name, ability, level, health, mana, magic_power):
        super().__init__(name, ability, level, health, mana)
        self.magic_power = magic_power


## Polimorfismo
'''
Permite que objetos de diferentes clases, sean tratados como de una clase común.
Esto se logra mediante la herencia y la sobreescritura de métodos.
El polimorfismo permite utilizar una misma interfaz para diferentes tipos de objetos.
'''
class Player: # <--- Clase Base 
    def __init__(self, name, ability, level, health, mana):
        self.__name = name
        self.__ability = ability
        self.__level = level
        self.__health = health
        self.__mana = mana
    def attack(self, enemy):
        f"{self.__name} ataca a {enemy}"

class Magician(Player): # <--- Clase Heredada
    def __init__(self, name, ability, level, health, mana, magic_power):
        super().__init__(name, ability, level, health, mana)
        self.magic_power = magic_power
    def attack(self, enemy):
        return f"{self.__name} invoca un poder desconocido hacia {enemy}"
p5 = Magician("Gandalf", 100, 50, 20, 250, 500)

class Warrior(Player): # <--- Clase Heredada
    def __init__(self, name, ability, level, health, mana, force):
        super().__init__(name, ability, level, health, mana)
        self.force = force
    def attack(self, enemy):
        return f"{self.__name} arremete contra {enemy}"

p6 = Warrior("Leonidas", 120, 42, 50, 10, 500)

def stroke(player, enemy):
    print("Te lanzaré mi mejor ataque")
    print(player.attack(enemy))
