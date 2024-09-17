import random
import math

# Implementación del experimento de la aguja de Buffon
def monte_carlo_buffon_needle(num_throws, needle_length, line_distance):
    crosses = 0

    for _ in range(num_throws):
        # Elegir aleatoriamente la distancia del centro de la aguja a la línea más cercana
        distance_to_line = random.uniform(0, line_distance / 2)
        
        # Elegir aleatoriamente el ángulo entre la aguja y las líneas
        angle = random.uniform(0, math.pi / 2)

        # Comprobar si la aguja cruza una línea
        if distance_to_line <= (needle_length / 2) * math.sin(angle):
            crosses += 1

    # Estimación de Pi utilizando la fórmula de Buffon
    return (2 * needle_length * num_throws) / (crosses * line_distance) if crosses > 0 else float('inf')

# Parámetros
num_throws = 100000  # Número de lanzamientos de la aguja
needle_length = 1.0  # Longitud de la aguja
line_distance = 1.0  # Distancia entre las líneas

# Estimar Pi con el experimento de Buffon
approx_pi = monte_carlo_buffon_needle(num_throws, needle_length, line_distance)

# Valor de Pi original con 20 decimales
pi_original = 3.14159265358979323846

# Calcular el porcentaje de error
error_percentage = abs((approx_pi - pi_original) / pi_original) * 100
approx_pi, error_percentage

print(approx_pi)
print(error_percentage)