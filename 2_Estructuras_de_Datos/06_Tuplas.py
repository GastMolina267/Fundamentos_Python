### Tuplas ###
## Una tupla es una colección de diferentes tipos de datos que está ordenada e inmutable

# Creación de una tupla
empty_tuple = ()
tpl = ('item1', 'item2','item3')
# ó usando el constructor de la tupla
empty_tuple = tuple()

# Segmentación de tuplas
# Podemos dividir una subtupla especificando un rango de índices donde comenzar y dónde terminar
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # todos los items
all_items = tpl[0:]         # todos los items
middle_two_items = tpl[1:3]  # no incluye artículo en el índice 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # todos los items
all_fruits= fruits[0:]      # todos los items
orange_mango = fruits[1:3]  # no incluye artículo en el índice 3
orange_to_the_rest = fruits[1:]

# Cambiar tuplas a listas
# Podemos cambiar las tuplas a listas y las listas a tuplas.
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# Unión de tuplas
# Podemos unir dos o más tuplas usando el operador +.
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
