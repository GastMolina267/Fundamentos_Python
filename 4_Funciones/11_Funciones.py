### Funciones ###
## Una función es un bloque reutilizable de código o instrucciones de programación 
# diseñado para realizar una determinada tarea

# Declarar y llamar a una función
'''Declarando la función
def function_name():
    codes
    codes'''

'''Llamando a la función
function_name()'''

## Tipos de funciones

# Función sin parámetros
def generate_full_name ():
    first_name = 'Marco'
    last_name = 'Aurelio'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # Llamando a la función

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# Función que devuelve un valor 
def generate_full_name ():
    first_name = 'Marco'
    last_name = 'Aurelio'
    space = ' '
    full_name = first_name + space + last_name
    return full_name # <------- Retorna 
print(generate_full_name()) 

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

## Función con parámetros
'''
Parámetro único: Si nuestra función toma un parámetro, debemos llamar a nuestra función con un argumento.
'''
# Declarando la función
def function_name(parameter):
    '''
    codes
    codes
    '''
# Llamando la función
print(function_name('argument'))

def greetings (name):
    message = name + ', Bienvenido a Python!'
    return message

print(greetings('Aurelio'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

## Dos parámetros
'''
Si nuestra función toma varios parámetros, debemos llamarla con argumentos
'''
  # Declaring a function
def function_name(para1, para2):
    '''
    codes
    codes
    '''
  # Calling function
print(function_name('arg1', 'arg2'))

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Nombre completo: ', generate_full_name('Marco','Aurelio'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Suma de dos números: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Peso del objeto en Newtons: ', weight_of_object(100, 9.81))


# Pasar argumentos con clave y valor
'''
Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa
'''
# Declaring a function
def function_name(para1, para2):
    '''
    codes
    codes
    '''
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # El orden de los argumentos no importa aquí

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Marco', lastname = 'Aurelio'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) 