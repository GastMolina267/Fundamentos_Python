### Sets/Conjunto ###
## Set es una colección de elementos distintos desordenados y no indexados. 

# Creación de un conjunto
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
# ó usando el constructor del set
st = set()

# Acceso a los elementos de un conjunto
# Usamos bucles para acceder a los elementos.

### Algunas funciones del Set ###

# add()
# Una vez que se crea un conjunto, no podemos cambiar ningún elemento y también podemos agregar elementos adicionales
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

# update()
# Permite agregar varios elementos a un conjunto. El update() toma un argumento de lista.
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

# remove() 
# Eliminar un elemento de un conjunto
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# pop()
# Elimina un elemento aleatorio de una lista y devuelven el elemento eliminado.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # Remueve un item aleatorio del Set

# union()
# Podemos unir dos conjuntos usando el método union() o update().
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

### Entre otros muchos métodos ###