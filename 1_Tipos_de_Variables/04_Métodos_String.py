### Métodos de Strings ###

# capitalize()
# Convierte el primer carácter de la cadena en mayúscula
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count()
# Devuelve las apariciones de la subcadena en la cadena
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2

# endswith()
# Comprueba si una cadena termina con una terminación especificada.
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs()
# Reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find()
# Devuelve el índice de la primera aparición de una subcadena, si no se encuentra devuelve -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# rfind()
# Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1.
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

# format()
# Formatea la cadena en una salidamás agradable.
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

# index()
# Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final (por defecto 0 y longitud de cadena - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error

# rindex()
# Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error

# isalnum()
# Comprueba el carácter alfanumérico
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha()
# Comprueba si todos los elementos de la cadena son caracteres alfabéticos (a-z y A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal()
# Comprueba si todos los caracteres de una cadena son decimales (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

# join()
# Devuelve una cadena concatenada
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

# replace()
# Reemplaza la subcadena con una cadena dada
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# title()
# Devuelve una cadena con mayúsculas y minúsculas de título
challenge = 'esto es un ejemplo de python'
print(challenge.title()) # Esto Es Un Ejemplo De Python

# swapcase()
# Convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas en mayúsculas
challenge = 'esto es un ejemplo de python'
print(challenge.swapcase())   # ESTO ES UN EJEMPLO DE PYTHON
challenge = 'Esto Es Un Ejemplo De Python'
print(challenge.swapcase())  # eSTO eS uN eJEMPLO dE pYTHON

# startswith()
# Comprueba si la cadena comienza con la cadena especificada
challenge = 'Esto es un ejemplo de python'
print(challenge.startswith('python')) # True

challenge = 'Esto es un ejemplo de python'
print(challenge.startswith('This is')) # False

# upper()
# Convierte todos los caracteres alfabéticos de la cadena en mayúscula
texto = "Hola, mundo!"
texto_mayusculas = texto.upper() # HOLA, MUNDO!