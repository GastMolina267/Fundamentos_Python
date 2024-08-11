### PANDAS ###
## Tratar con DATOS faltantes
import pandas as pd
import numpy as np

df = pd.DataFrame({'A' : [1, 2, np.nan, 4], 'B' : [5, np.nan, 7, 8], 'C' : [9, 10, 11, 12]})
print(df)
print(df.isnull()) ## Sirve para que vaya recorriendo el DataFrame y determinar si hay datos NULOS
'''
print(df.notnull()) ## Es la contraparte a isnull() 
'''
print(df.isnull().sum()) ## Sirve para indicarnos cuántos valores nulos hay en cada fila

df_drop = df.dropna()
print(df_drop)

df_drop_column = df.dropna(axis=1) ## El atributo axis=0 indicaría las filas, y axis=1 indicaría las columnas
print(df_drop_column)

df_fill = df.fillna(value=0) ## Sirve para completar aquellos espacios vacíos en el DataFrame con value=
print(df_fill)
'''
df_fill = df.fillna(method='ffill') ## Completa los espacios vacíos con el núm que está arriba de la celda
df_fill = df.fillna(method='bfill') ## Completa los espacios vacíos con el núm que está debajo de la celda
df_fill = df.fillna(df.mean()) ## Completa los espacios vacíos con el promedio entre los demás dígitos de la columna
df_fill = df.interpolate() ## Completa los espacios vacíos evaluando cuál sería el número más óptimo por lógico
Ejemplo de interpolate() -> Si tengo en un columna 1, 2, NaN, 4 ; se deduce que el núm más óptimo sería 3
'''