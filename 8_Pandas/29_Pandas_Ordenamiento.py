### PANDAS ###
## Ordenamiento y Rankeo de DATOS
import pandas as pd

data = {'Nombre' : ['Milei', 'Sánchez', 'Bukele', ' Trump', 'Maduro'],
        'Aura' : [100, 10, 50, 75, -20],
        'País' : ['ARG', 'ESP', 'ESL', 'EEUU', 'VLZ']}

df = pd.DataFrame(data)
print(df)
print("----------------------")
df = df.sort_values(by="Aura") ## sort_values sirve para ordenar (predeterminadamente) de manera descendes los datos
## Desde los menores hasta los mayores, o alfabéticamente si son strings
print(df)
'''
df = df.sort_values(by="Aura", ascending=False) los ordenaría de mayor a menor
df = df.sort_values(by="País", ascending=True) los ordenaría alfabéticamente A-Z
df = df.sort_values(by="País", ascending=False) los ordenaría alfabéticamente Z-A
df = df.sort_values(by=['Aura', 'País']) los ordena primeramente por Aura de menor a mayor, y después (si es hay valores de Aura iguales) ordena alfabéticamente de la A-Z
'''
df['Ranking_Aura'] = df['Aura'].rank() ## rank() permite rankear desde el menor hasta el mayor
## Si fuesen edades, sería desde el más joven hasta el más viejo
print(df)