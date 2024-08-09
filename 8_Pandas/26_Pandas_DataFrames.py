### PANDAS ###
import pandas as pd
import numpy as np
## Formas de hacer un DataFrame

datos1 = {
    'Nombres' : ['Fernandez', 'Maduro', 'Milei', 'Sánchez'],
    'Aura' : [10, -10, 100, 5]
}

df = pd.DataFrame(datos1)
print(df)
print("---------------------------------")
datos2 = [
    {'Nombre' : 'Fernandez', 'Aura' : 10},
    {'Nombre' : 'Maduro', 'Aura' : -10},
    {'Nombre' : 'Milei', 'Aura' : 100},
    {'Nombre' : 'Sánchez', 'Aura' : 5},
]
df2 = pd.DataFrame(datos2)
print(df2)
print("---------------------------------")

datos3 = np.array([[1,2,3],[4,5,6]])
df3 = pd.DataFrame(datos3)
print(df3)
print("---------------------------------")
# DataSet descargado desde Kaggle
kaggle = pd.read_csv("./Media/powerlifting_dataset.csv")
print(kaggle)
print("---------------------------------")

df4 = pd.DataFrame(datos2)
# Agregamos una nueva columna al DataFrame y completamos los datos
df4["Nacionalidad"] = ["Argentina", "Venezolano", "Argentino", "Español"]
# Creando una nueva fila (que vendría a ser un nuevo diccionario) y concatenando al DataFrame
nueva_fila = pd.DataFrame({'Nombre':'Bukele', 'Aura': 50, 'Nacionalidad':'Salvadoreño'}, index=[4])
df4 = pd.concat([df4, nueva_fila])
# Si pusiesemos el index mal, tendríamos dos filas con el mismo índice (lo cuál sería confuso al momento de localizarlos)
nueva_fila2 = pd.DataFrame({'Nombre':'Trump', 'Aura': 70, 'Nacionalidad':'EEUU'}, index=[4])
# Agregamos reset_index(drop=True)
'''
Sirve para resetear los index y se auto-acomoden solos
'''
df4 = pd.concat([df4, nueva_fila2]).reset_index(drop=True)
print(df4)