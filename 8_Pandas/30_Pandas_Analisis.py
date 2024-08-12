### PANDAS ###
## Análisis Exploratorio
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'A' : [1,2,3,4,5],
    'B' : [2,3,4,5,6],
    'C' : [1,2,3,2,1]
})

print(df)
print("-------------------")
print(df.describe()) ## Realiza un análisis descriptivo de los DATOS
# Como pueden ser el promedio, el mínimo, el máximo, la desviación estándar, los qintales
'''
Son otras formas de análisis particular
print(df['A'].mean())
print(df['A'].median())
print(df['A'].node())
print(df['A'].std())
print(df['A'].var())
print(df['A'].min())
print(df['A'].max())
print(df['A'].quantile(0.25))

Sirve para indicar la cantidad de valores únicos en cierta columna
print(df['C'].nunique())

Sirve para indicar la cantidad de veces que aparece cierto valor en cierta columna
print(df['C'].value_counts())

Sirve para indicar la correlación entre dos columnas, es decir, las similitudes que guardan
Por ejemplo, un tipo de relación puede ser la forma en la distribución de sus valores o el orden de crecimiento de los mismos
print(df['A'].corr(df['B']))
'''
print("-------------------")
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True) ## Crear un mapa de calor para ver las correlaciones
plt.show()

df['A'].plot.line() ## Crea un gráfico de línea
'''
Le podemos dar formato a este gráfico de línea
df['A].plot.line(color="red", title="Line Plot", xlabel="Index", ylabel="Valors")
'''
plt.show() 

df['C'].plot.hist() ## Crea un gráfico de barras
plt.show() 

df.plot.scatter(x='A', y='C') ## Crea un gráfico de puntos
plt.show()

df['A'].plot.box() ## Crea un gráfico de caja 
plt.show()

df.plot.area() ## Crea un gráfico de áreas
plt.show()

df['A'].plot.pie() ## Crea un gráfico de torta
plt.show()