import pandas as pd

## Formas de hacer un DataFrame

datos1 = {
    'Nombres' : ['Fernandez', 'Maduro', 'Milei', 'Sánchez'],
    'Aura' : [10, -10, 100, 5]
}

df = pd.DataFrame(datos1)
print(df)

datos2 = [
    {'Nombre' : 'Fernandez', 'Aura' : 10},
    {'Nombre' : 'Maduro', 'Aura' : -10},
    {'Nombre' : 'Milei', 'Aura' : 100},
    {'Nombre' : 'Sánchez', 'Aura' : 5},
]
df2 = pd.DataFrame(datos2)
print(df2)