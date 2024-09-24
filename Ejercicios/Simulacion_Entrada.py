import random
import matplotlib.pyplot as plt

# Parámetros de simulación
TIEMPO_SIMULACION = 480  # 8 horas (en minutos)

# Inicialización de variables
reloj = 0
E = 0  # Estado del empleado (0=libre, 1=ocupado)
Q = 0  # Número de clientes en la cola
D = 0  # Tiempo total de espera en la cola
R = 0  # Tiempo acumulado de clientes en la cola (área bajo Q(t))
n = 0  # Número de clientes atendidos
total_espera = 0  # Tiempo total de espera para cada cliente
num_clientes_espera = 0  # Número de clientes que tuvieron que esperar
tiempos_cola = []  # Para almacenar el número de clientes en la cola

# Inicializar lista de eventos
llegada = random.expovariate(1/10)  # Tiempo entre llegadas promedio de 10 minutos
marcha = None  # Tiempo de marcha del cliente actual

# Funciones para generar tiempos aleatorios
def generar_tiempo_llegada(media):
    return random.expovariate(1/media)

def generar_tiempo_servicio(media):
    return random.expovariate(1/media)

# Bucle de simulación
while reloj < TIEMPO_SIMULACION:
    if marcha is None or (llegada <= marcha and llegada <= TIEMPO_SIMULACION):
        # Evento de llegada de cliente
        reloj = llegada
        if E == 0:  # Empleado libre
            E = 1  # Empleado ocupado
            n += 1  # Incremento del número de clientes atendidos
            S1 = generar_tiempo_servicio(5)  # Tiempo de servicio promedio 5 minutos
            marcha = reloj + S1  # Programar el evento de marcha
        else:
            # Actualizar la cola (área bajo Q(t) antes de incrementar)
            R += Q * (reloj - llegada if llegada > 0 else 0)  # Evitar valores negativos
            Q += 1  # Incrementar tamaño de la cola

        llegada = reloj + generar_tiempo_llegada(10)  # Programar próxima llegada

    elif marcha is not None and marcha <= TIEMPO_SIMULACION:
        # Evento de marcha del cliente
        reloj = marcha
        if Q > 0:  # Si hay clientes en cola
            # Actualizar la cola y tiempos de espera
            R += Q * (reloj - llegada if llegada > 0 else 0)  # Evitar valores negativos
            Q -= 1  # Reducir el tamaño de la cola
            n += 1
            tiempo_espera = max(reloj - llegada, 0)  # Evitar valores negativos
            total_espera += tiempo_espera  # Tiempo de espera del cliente
            num_clientes_espera += 1  # Contar cliente que esperó
            S1 = generar_tiempo_servicio(5)  # Generar tiempo de servicio
            marcha = reloj + S1  # Programar nueva marcha
        else:
            # No hay clientes en la cola, liberar al empleado
            E = 0
            marcha = None

    else:
        # Salir si no hay más eventos en tiempo de simulación
        break
    
    # Guardar número de clientes en cola para análisis gráfico
    tiempos_cola.append(Q)

# Resultados de la simulación
promedio_espera = total_espera / num_clientes_espera if num_clientes_espera > 0 else 0
promedio_clientes_cola = R / TIEMPO_SIMULACION if R >= 0 else 0  # Evitar negativos

# Imprimir resultados corregidos
print(f"Clientes atendidos: {n}")
print(f"Tiempo total de espera en cola: {total_espera:.2f} minutos")
print(f"Promedio de tiempo de espera por cliente: {promedio_espera:.2f} minutos")
print(f"Promedio de clientes en cola: {promedio_clientes_cola:.2f}")
print(f"Área bajo Q(t) (clientes en cola a lo largo del tiempo): {R:.2f}")

# Graficar el número de clientes en la cola durante la simulación
plt.plot(tiempos_cola)
plt.title('Evolución del número de clientes en cola durante la simulación')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Número de clientes en cola')
plt.grid(True)
plt.show()
