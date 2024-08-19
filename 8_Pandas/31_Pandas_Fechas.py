### PANDAS ###
## Trabajando con fechas de DATOS
from datetime import datetime
import pandas as pd
import numpy as np

##  Instalar Jupyter Notebook

# Convertir cadena de texto a datatime
fecha_str = '2024-13-08 9:30:00:00'
fecha_dt = pd.to_datetime(fecha_str)
print(type(fecha_dt))
print(type(fecha_str))