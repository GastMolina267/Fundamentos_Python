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