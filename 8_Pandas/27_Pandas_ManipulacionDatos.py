### PANDAS ### 
## Técnicas para la manipulación de DATOS
import pandas as pd

data = {'Nombre' : ['Milei', 'Sánchez', 'Bukele', ' Trump', 'Maduro'],
        'Aura' : [100, 10, 50, 75, -20],
        'País' : ['ARG', 'ESP', 'ESL', 'EEUU', 'VLZ']}

data2 = {'Nombre' : ['Milei', 'Sánchez', 'Bukele', ' Trump', 'Maduro', 'Putin', 'Biden', 'Fernandez'],
        'Aura' : [100, 10, 50, 75, -20, 50, 20, -100],
        'País' : ['ARG', 'ESP', 'ESL', 'EEUU', 'VLZ', 'RUS', 'EEUU', 'ARG']}

def convertir_mayus(x): 
    return x.upper()

df = pd.DataFrame(data)
print(df)
print("-------------------------")
df['Aura'] = df['Aura'].apply(lambda x: x + 10) ## Permite modificar una columna, y agregarle un parámetro
'''
En este caso, a la columna Aura, le agregamos una función en la que a los valores actuales de la columna,
se le suma 10
'''
print(df)
print("-------------------------")
df_funcion = pd.DataFrame(data2)
df_funcion['Nombre'] = df_funcion['Nombre'].apply(convertir_mayus)
## Pasamos como parámetros los elementos de la columna Nombre, para volverlos mayúsculas
print(df_funcion)

'''
promedio_aura = df['Aura'].mean() # De la columna Aura, retornar el promedio
max_aura = df['Aura'].max() # De la columna Aura, retornar el valor máximo
df['Nombre'] = df['Nombre'].replace('Fernandez', 'Peron')
'''