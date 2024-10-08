import matplotlib.pyplot as plt
import numpy as np

# Parámetros del generador
a = 9
b = 0
x = 3
m = 13

# Listas para almacenar los valores generados
ri_values = []

# Generar la secuencia pseudoaleatoria
for i in range(1000):  # Aumentamos las iteraciones para mejor análisis
    x = (a * x + b) % m
    ri = x / m
    ri_values.append(ri)

# Convertir a numpy array para análisis
ri_values = np.array(ri_values)

# Crear figura para múltiples gráficos
plt.figure(figsize=(14, 8))

# Subplot 1: Gráfico de línea de los valores pseudoaleatorios
plt.subplot(2, 2, 1)
plt.plot(ri_values, marker='o', linestyle='-', color='b', label='Valores pseudoaleatorios')
plt.xlabel('Iteración')
plt.ylabel('Valor pseudoaleatorio (x/m)')
plt.title('Generador Congruencial Lineal')
plt.grid(True)
plt.legend()

# Subplot 2: Histograma de la distribución de los valores pseudoaleatorios
plt.subplot(2, 2, 2)
plt.hist(ri_values, bins=10, color='g', edgecolor='black', alpha=0.7)
plt.xlabel('Valor pseudoaleatorio (x/m)')
plt.ylabel('Frecuencia')
plt.title('Histograma de la distribución')

# Subplot 3: Autocorrelación de los valores pseudoaleatorios
plt.subplot(2, 2, 3)
autocorr = np.correlate(ri_values - np.mean(ri_values), ri_values - np.mean(ri_values), mode='full')
autocorr = autocorr[autocorr.size // 2:]  # Usar solo la mitad positiva
autocorr /= autocorr[0]  # Normalizar
plt.plot(autocorr, color='r', label='Autocorrelación')
plt.xlabel('Lag')
plt.ylabel('Autocorrelación')
plt.title('Autocorrelación de los valores pseudoaleatorios')
plt.grid(True)
plt.legend()

# Subplot 4: Calcular y mostrar la media y varianza
mean_value = np.mean(ri_values)
variance_value = np.var(ri_values)

plt.subplot(2, 2, 4)
plt.text(0.1, 0.6, f'Media: {mean_value:.4f}', fontsize=14)
plt.text(0.1, 0.4, f'Varianza: {variance_value:.4f}', fontsize=14)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis('off')
plt.title('Media y Varianza de los valores pseudoaleatorios')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
