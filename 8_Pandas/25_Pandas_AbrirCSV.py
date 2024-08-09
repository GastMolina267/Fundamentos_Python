### PANDAS ###
import pandas as pd

df = pd.read_csv("./Media/data.csv")
'''
    Si nos diese un error porque el archivo tiene una codificación utf-8
    agregar read_csv("ruta del archivo csv", encoding="ISO-8859-1")
'''
print(df.columns)
print(df.head())
# La función head() nos muestra los primeros 5 datos

print(df.shape)
# La función shape nos muestra la cantidad de filas y columnas que tiene el archivo

df_ordenado = df.sort_values('Maxpulse')
# La función sort_values() ordena de menor a mayor (en caso de valores numéricos) y en orden alfabético (en caso de nombres)
print(df_ordenado.head())

df_filtrado = df[df['Maxpulse'] > 150]
# Es una de acceder a cierta columna y de filtrar que tipo de datos quiero que se muestren
print(df_filtrado)
