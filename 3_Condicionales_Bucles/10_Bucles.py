### Bucles ###
## Para manejar tareas repetitivas, los lenguajes de programación utilizan bucles

# Bucle while
# Se utiliza para ejecutar un bloque de instrucciones repetidamente hasta que se satisfaga una condición determinada
'''while condition:
    code goes here'''

count = 0
while count < 5:
    print(count)
    count = count + 1
# Si estamos interesados en ejecutar un bloque de código una vez que la condición ya no es verdadera, podemos usar else
'''while condition:
    code goes here
else:
    code goes here'''

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Romper y continuar - Parte 1
    # Break: Usamos break cuando nos gusta salir o detener el bucle
    '''while condition:
        code goes here
        if another_condition:
            break'''

    count = 0
    while count < 5:
        print(count)
        count = count + 1
        if count == 3:
            break
    # El bucle while anterior solo imprime 0, 1, 2, pero cuando llega a 3 se detiene.

    # Continue: Con la instrucción continue podemos omitir la iteración actual y continuar con la siguiente
    '''while condition:
        code goes here
        if another_condition:
            continue'''
    
    count = 0
    while count < 5:
        if count == 3:
            count = count + 1
            continue
        print(count)
        count = count + 1
    # El bucle while anterior solo imprime 0, 1, 2 y 4 (omite 3)

# Bucle for
# El bucle se utiliza para iterar sobre una secuencia (que puede ser una lista, una tupla, un diccionario, un conjunto o una cadena)
    # Bucle For con lista
    '''for iterator in lst:
        code goes here'''

    '''for iterator in lst:
        code goes here'''
    
    # Bucle For con cadena
    '''for iterator in string:
        code goes here'''

    language = 'Python'
    for letter in language:
        print(letter)


    for i in range(len(language)):
        print(language[i])

    # Bucle For con tupla
    '''for iterator in tpl:
        code goes here'''

    numbers = (0, 1, 2, 3, 4, 5)
    for number in numbers:
        print(number)

    # Bucle For con diccionario
    '''for iterator in dct:
        code goes here'''

    person = {
        'first_name':'Asabeneh',
        'last_name':'Yetayeh',
        'age':250,
        'country':'Finland',
        'is_marred':True,
        'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'street':'Space street',
            'zipcode':'02210'
        }
    }
    for key in person:
        print(key)

    for key, value in person.items():
        print(key, value) 

    # Bucles en el conjunto
    '''for iterator in st:
        code goes here'''

    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    for company in it_companies:
        print(company)

# Romper y continuar - Parte 2
    # Break: Usamos el break cuando nos gusta detener nuestro bucle antes de que se complete
    '''for iterator in sequence:
        code goes here
        if condition:
            break'''

    numbers = (0,1,2,3,4,5)
    for number in numbers:
        print(number)
        if number == 3:
            break
    # En el ejemplo anterior, el bucle se detiene cuando llega a 3

    # Continue: Usamos continuar cuando nos gusta omitir algunos de los pasos en la iteración del bucle
    '''for iterator in sequence:
        code goes here
        if condition:
            continue'''

    numbers = (0,1,2,3,4,5)
    for number in numbers:
        print(number)
        if number == 3:
            continue
        print('El siguiente número debería ser ', number + 1) if number != 5 else print("final del bucle") 
    print('fuera del bucle')
    # En el ejemplo anterior, si el número es igual a 3, se omite el paso después de la condición (pero dentro del bucle) y la ejecución del bucle continúa si quedan iteraciones

# Bucle For anidado
'''for x in y:
    for t in x:
        print(t)'''

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)