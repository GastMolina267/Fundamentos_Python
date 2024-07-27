### Condicionales ###
## Las instrucciones en el script de Python se ejecutan secuencialmente de arriba a abajo

### Tipos de condicionales ###

# If
# La palabra clave if se usa para verificar si una condición es verdadera y para ejecutar el código del bloque
'''if condition:
    this part of code runs for truthy conditions'''

a = 3
if a > 0:
    print('Es un número positivo')


# Else
# Si la condición es verdadera, se ejecutará el primer bloque, si no, se ejecutará la condición else
'''if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions'''

a = 3
if a < 0:
    print('Es un número negativo')
else:
    print('Es un número positivo')

# Elif Else
# Usamos elif cuando tenemos varias condiciones
'''if condition:
    code
elif condition:
    code
else:
    code'''

a = 0
if a > 0:
    print('Es un número positivo')
elif a < 0:
    print('Es un número negativo')
else:
    print('Es cero')

# Taquigrafía
'''code if condition else code'''

a = 3
print('Es un positivo') if a > 0 else print('Es un negativo') 

# Condiciones anidadas
'''if condition:
    code
    if condition:
    code'''

a = 0
if a > 0:
    if a % 2 == 0:
        print('Es un número positivo entero')
    else:
        print('Es un número positivo')
elif a == 0:
    print('Es cero')
else:
    print('Es un número negativo')

# Operadores lógicos y de condición If
'''if condition and condition:
    code'''

a = 0
if a > 0 and a % 2 == 0:
        print('A es un número entero par y positivo')
elif a > 0 and a % 2 !=  0:
     print('A es un entero positivo')
elif a == 0:
    print('A es un cero')
else:
    print('A es negativo')

# Operadores lógicos If y Or
'''if condition or condition:
    code'''

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Acceso garantizado!')
else:
    print('Acceso denegado!')
