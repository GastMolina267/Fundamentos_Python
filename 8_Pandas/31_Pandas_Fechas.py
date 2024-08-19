from datetime import datetime
import pandas as pd
import numpy as np

# %%
# Convertir cadena de texto a datatime
fecha_str = '2024-08-13 09:30:00'
fecha_dt = pd.to_datetime(fecha_str)
## Objetos diferentes
print(fecha_dt)
print(fecha_str)

# %%
# Creando un objeto Timestamp en Pandas
timestap = pd.Timestamp(datetime.now())
print(timestap)

# %%
# Creando un DatatimeIndex en Pandas
meses = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
print(meses)

# %%
dias = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
print(dias)

# %%
dias = pd.date_range(start='2024-01-01', end='2024-01-31', freq='H')
print(dias)

# %%
# Creación de series de tiempo
serie = pd.Series(np.random.rand(len(meses)), index=meses)
print(serie)

# %%
from datetime import timedelta
# Creando un objeto timedelta
# Creando un objeto Timestamp en Pandas
timestap = pd.Timestamp(datetime.now())
print(timestap)
delta = timedelta(days=7)
print(delta)
nueva_fecha = timestap + delta
print(nueva_fecha)

# %%
# Suponiendo que 'precios' es nuestra serie de tiempo de precios de cierre diarios
precios = pd.Series(np.random.rand(100), index=pd.date_range(start='2024-01-01', periods=100, freq='D'))
print(precios)
# Calcular la media móvil de los últimos 7 días
media_movil = precios.rolling(window=7).mean()
print(media_movil.head(7))

# %%
import matplotlib.pyplot as plt

# Trazar la serie de tiempo de precios y la media móvil
plt.figure(figsize=(12,6))
precios.plot(label='Precio de cierre')
media_movil.plot(label='Media móvil de 7 días')
plt.title('Precio de cierre y media móvil de 7 días')
plt.legend()
plt.show()