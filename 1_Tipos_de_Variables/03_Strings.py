### Strings ###

# Concatenación de Strings
nombre = 'Asabeneh'
apellido = 'Yetayeh'
space = ' '
nombre_completo = nombre  +  space + apellido
print(nombre_completo) # Asabeneh Yetayeh
# Comprobar la longitud de una cadena usando la función incorporada len()
print(len(nombre))  # 8
print(len(apellido))   # 7
print(len(nombre) > len(apellido)) # True
print(len(nombre_completo)) # 16

print("<------------------------------------------------->")
# Secuencia de Tab/Espaciados
print('Espero que todas estén disfrutando del Desafío Python.\nAre you ?') # Línea de quiebre
print('Días\tTopicos\tEjercicios') # Agregar 4 espacios de Tab 
print('Días 1\t5\t5')
print('Días 2\t6\t20')
print('Días 3\t5\t23')
print('Días 4\t1\t35')
print('Este es un símbolo de barra invertida (\\)')
print('En todos los lenguajes de programación comienza con \"Hello, World!\"')

print("<------------------------------------------------->")
# Nuevo formato de string de estilo (str.format)
nombre = 'Gastón'
apellido = 'Molina'
language = 'Python'
formated_string = 'Yo soy {} {}. Yo enseño {}'.format(nombre, apellido, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # Lo limita a dos dígitos después del decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

print("<------------------------------------------------->")
# Strings  y números
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'El área del círculo con radio {} es {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

print("<------------------------------------------------->")
# Desempaquetando carácteres
language = 'Python'
a,b,c,d,e,f = language # Asignando carácteres a variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

print("<------------------------------------------------->")
# Acceso a caracteres en cadenas por índice
language = 'Python'
primera_letra = language[0]
print(primera_letra) # P
segunda_letra = language[1]
print(segunda_letra) # y
ultimo_índice = len(language) - 1
ultima_letra = language[ultimo_índice]
print(ultima_letra) # n

print("<------------------------------------------------->")
#Si queremos empezar desde el extremo derecho, podemos usar la indexación negativa. -1 es el último índice.
language = 'Python'
ultima_letra = language[-1]
print(ultima_letra) # n
penúltima = language[-2]
print(penúltima) # o

print("<------------------------------------------------->")