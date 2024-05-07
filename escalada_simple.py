import random

# Función para calcular la distancia total de la ruta
def calcular_distancia(ruta, distancias):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancias[ruta[i]][ruta[i+1]]
    distancia_total += distancias[ruta[-1]][ruta[0]]  # Regresar a la ciudad de origen
    return distancia_total

# Función para generar una nueva ruta intercambiando dos ciudades
def generar_nueva_ruta(ruta):
    nueva_ruta = ruta[:]
    ciudad1 = random.randint(0, len(ruta) - 1)
    ciudad2 = ciudad1
    while ciudad2 == ciudad1:
        ciudad2 = random.randint(0, len(ruta) - 1)
    nueva_ruta[ciudad1], nueva_ruta[ciudad2] = nueva_ruta[ciudad2], nueva_ruta[ciudad1]
    return nueva_ruta

# Función para realizar la búsqueda escalada simple
def busqueda_escalada_simple(distancias, ruta_inicial):
    ruta_actual = ruta_inicial
    while True:
        nueva_ruta = generar_nueva_ruta(ruta_actual)
        if calcular_distancia(nueva_ruta, distancias) < calcular_distancia(ruta_actual, distancias):
            ruta_actual = nueva_ruta
        else:
            return ruta_actual

# Definir las distancias entre las ciudades
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Definir la ruta inicial
ruta_inicial = [0, 1, 2, 3]

# Llamar a la función de búsqueda escalada simple y pasar la ruta inicial
ruta_optima = busqueda_escalada_simple(distancias, ruta_inicial)

# Imprimir la ruta óptima
print("La ruta óptima es:", ruta_optima)
