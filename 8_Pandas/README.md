# Tema 8: Pandas Avanzado 🐼📊

## Introducción
Pandas es una biblioteca de Python esencial para el análisis y manipulación de datos. Este README cubre conceptos avanzados de Pandas, proporcionando una guía completa para el manejo eficiente de datos estructurados.

## Contenido 📚🔬
1. [Manipulación Avanzada de DataFrames](#manipulación-avanzada-de-dataframes)
2. [Análisis de Series Temporales](#análisis-de-series-temporales)
3. [Agrupación y Agregación](#agrupación-y-agregación)
4. [Manejo de Datos Faltantes](#manejo-de-datos-faltantes)
5. [Optimización de Rendimiento](#optimización-de-rendimiento)
6. [Entrada/Salida Avanzada](#entradaSalida-avanzada)
7. [Visualización de Datos](#visualización-de-datos)
8. [Técnicas de Limpieza de Datos](#técnicas-de-limpieza-de-datos)
9. [Funcionalidades Experimentales](#funcionalidades-experimentales)
10. [Proyectos Prácticos](#proyectos-prácticos)

## Manipulación Avanzada de DataFrames

### Fusión y Unión de DataFrames
```python
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2']})

result = pd.concat([df1, df2], axis=1)
```

### Pivoting y Unpivoting
```python
# Pivoting
pivoted = df.pivot(index='date', columns='variable', values='value')

# Unpivoting
melted = pd.melt(pivoted, id_vars=['date'], var_name='variable', value_name='value')
```

## Análisis de Series Temporales

### Creación de DatetimeIndex
```python
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
```

### Resampleo
```python
# Resampleo a frecuencia mensual
monthly = df.resample('M').mean()
```

## Agrupación y Agregación

### GroupBy Avanzado
```python
# Agrupación y múltiples agregaciones
result = df.groupby('category').agg({
    'sales': ['sum', 'mean'],
    'profit': ['min', 'max']
})
```

### Ventanas Móviles
```python
# Media móvil de 7 días
df['rolling_mean'] = df['value'].rolling(window=7).mean()
```

## Manejo de Datos Faltantes

### Imputación de Datos
```python
# Rellenar valores nulos con la media
df['column'].fillna(df['column'].mean(), inplace=True)

# Interpolación lineal
df['column'].interpolate(method='linear', inplace=True)
```

## Optimización de Rendimiento

### Uso de Categorías
```python
df['category'] = df['category'].astype('category')
```

### Cálculo Eficiente
```python
# Usar query para filtrado eficiente
result = df.query('column_a > 5 and column_b < 10')
```

## Entrada/Salida Avanzada

### Conexión con SQL
```python
import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_sql_query("SELECT * FROM table", conn)
```

## Visualización de Datos

### Gráficos Avanzados con Pandas
```python
import matplotlib.pyplot as plt

df.plot(kind='bar', stacked=True)
plt.title('Gráfico de Barras Apiladas')
plt.show()
```

## Técnicas de Limpieza de Datos

### Detección de Outliers
```python
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[~((df['column'] < (Q1 - 1.5 * IQR)) | (df['column'] > (Q3 + 1.5 * IQR)))]
```

## Funcionalidades Experimentales

### Uso de Extensiones
```python
# Ejemplo con una extensión hipotética
import pandas_extension

df.extension_method()
```

## Proyectos Prácticos

1. **Análisis de Datos Financieros**: Procesar y analizar datos históricos de acciones.
2. **Procesamiento de Logs**: Analizar logs de servidores para detectar patrones y anomalías.
3. **Análisis de Redes Sociales**: Procesar y visualizar datos de interacciones en redes sociales.

## Conclusión

Pandas es una herramienta poderosa y versátil para el análisis de datos en Python. A lo largo de este README, hemos cubierto conceptos avanzados que te permitirán realizar análisis de datos complejos y eficientes:

1. **Manipulación avanzada**: Aprendimos técnicas sofisticadas para trabajar con DataFrames.
2. **Series temporales**: Exploramos el manejo de datos temporales y técnicas de resampleo.
3. **Agrupación y agregación**: Descubrimos cómo realizar análisis detallados por grupos.
4. **Optimización**: Conocimos métodos para mejorar el rendimiento en grandes conjuntos de datos.
5. **Visualización**: Vimos cómo crear visualizaciones efectivas directamente desde Pandas.
6. **Limpieza de datos**: Aprendimos técnicas para preparar datos para análisis robustos.

Dominar estos conceptos avanzados de Pandas te permitirá abordar proyectos de análisis de datos más complejos y sofisticados. Recuerda que la práctica constante y la exploración de datos reales son clave para perfeccionar tus habilidades.

### Recursos Adicionales
- [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
- [Pandas Cookbook](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html)
- [Comunidad de Pandas en Stack Overflow](https://stackoverflow.com/questions/tagged/pandas)

💻📊 ¡FELIZ ANÁLISIS DE DATOS! 📊💻