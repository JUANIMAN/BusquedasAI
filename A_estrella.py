# Importamos la clase Grafo y la librería heapq
import grafo
import heapq


# Definimos la clase Nodo
class Nodo:
    def __init__(self, valor, padre=None):
        self.valor = valor  # Valor del nodo
        self.padre = padre  # Nodo padre
        self.g = 0  # Costo del camino desde el nodo inicial hasta el nodo actual
        self.h = 0  # Estimación del costo desde el nodo actual hasta el nodo final
        self.f = 0  # Costo total estimado del camino más barato pasando por el nodo actual: f = g + h

    # Método para comparar nodos
    def __eq__(self, otro):
        return self.valor == otro.valor

    # Método para ordenar nodos
    def __lt__(self, otro):
        return self.f < otro.f


# Definimos la función AEstrella
def AEstrella(grafo, nodo_inicial, nodo_final):
    # Creamos nodos para el nodo inicial y final
    nodo_inicial = Nodo(nodo_inicial)
    nodo_final = Nodo(nodo_final)

    # Inicializamos las listas abierta y cerrada
    lista_abierta = []
    lista_cerrada = []

    # Agregamos el nodo inicial a la lista abierta
    heapq.heappush(lista_abierta, nodo_inicial)

    # Mientras la lista abierta no esté vacía
    while len(lista_abierta) > 0:
        # Obtenemos el nodo actual de la lista abierta
        nodo_actual = heapq.heappop(lista_abierta)
        # Agregamos el nodo actual a la lista cerrada
        lista_cerrada.append(nodo_actual)
        print(f"Lista cerrada: {[nodo.valor for nodo in lista_cerrada]}")

        # Si el nodo actual es el nodo final, construimos la ruta
        if nodo_actual == nodo_final:
            print("Nodo final encontrado!")
            ruta = []
            while nodo_actual != nodo_inicial:
                ruta.append(nodo_actual.valor)
                nodo_actual = nodo_actual.padre
            ruta.append(nodo_inicial.valor)
            # Devolvemos la ruta en orden inverso
            return ruta[::-1]

        # Generamos los nodos vecinos
        vecinos = [Nodo(v, nodo_actual) for v in grafo.vecinos(nodo_actual.valor)]
        print(f"Vecinos del nodo {nodo_actual.valor}: {[v.valor for v in vecinos]}")

        # Para cada vecino
        for vecino in vecinos:
            # Si el vecino está en la lista cerrada, lo ignoramos
            if vecino in lista_cerrada:
                continue

            # Calculamos los valores g, h y f para el vecino
            vecino.g = nodo_actual.g + grafo.evaluar(nodo_actual.valor, vecino.valor)
            vecino.h = grafo.evaluar(vecino.valor, nodo_final.valor)
            vecino.f = vecino.g + vecino.h

            # Si el vecino ya está en la lista abierta y tiene un costo mayor, lo ignoramos
            if any(nodo_abierto == vecino and vecino.g > nodo_abierto.g for nodo_abierto in lista_abierta):
                continue

            # Agregamos el vecino a la lista abierta
            heapq.heappush(lista_abierta, vecino)
            print(f"Agregando el nodo {vecino.valor} a la lista abierta")

    # Si no se encontró una ruta, devolvemos None
    return None


# Creamos un grafo y realizamos la búsqueda por A*
grafo = grafo.Grafo()

# Definimos el nodo inicial y el nodo final
nodo_inicial = '8'
nodo_final = '18'

# Encontramos la ruta usando A*
print(f"Iniciando la búsqueda desde el nodo {nodo_inicial} hasta el nodo {nodo_final}")
ruta = AEstrella(grafo, nodo_inicial, nodo_final)

# Imprimimos la ruta
print(f"La ruta desde el nodo {nodo_inicial} hasta el nodo {nodo_final} es: {ruta}")
