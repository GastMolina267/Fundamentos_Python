### PANDAS ###
## Permite manejar y modificar datos de manera eficiente 
# Es perfecto para manejar datos tabulares, es decir que se puedan organizar en una tabla

import pandas as pd

serie = pd.Series([1,2,3,4,5,6,7,8,9,10]) # Es como una columna en Excel
print(serie)

datos = {
    'nombre' : ["Gaston", "Edgar", "Tomas", "Facundo", "Manue", "Gonza"],
    'edades' :  [23, 24, 25, 28, 29, 30]
}

df = pd.DataFrame(datos) 
# Creación de un DataFrame
# Un DataFrame es una serie de Series Pandas indexadas por un valor
# o bien es una colección de datos habitualmente tabulada
print(df)