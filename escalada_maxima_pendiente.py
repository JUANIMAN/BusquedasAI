# Importamos la clase Grafo
import grafo


# Definimos la clase BusquedaEscaladaMaximaPendiente
class BusquedaEscaladaMaximaPendiente:
    # Inicializamos la clase con el grafo, un conjunto para los nodos visitados y una lista para la ruta
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitado = set()
        self.ruta = []

    # Método para realizar la búsqueda
    def buscar(self, nodo_inicial, nodo_final, sentido_horario=True):
        # Establecemos el nodo actual como el nodo inicial y lo agregamos a la ruta
        nodo_actual = nodo_inicial
        self.ruta = [nodo_inicial]

        # Mientras el nodo actual no sea el nodo final
        while nodo_actual != nodo_final:
            # Inicializamos la menor distancia con infinito y el mejor vecino con None
            menor_distancia = float('inf')
            mejor_vecino = None
            # Obtenemos los vecinos del nodo actual
            vecinos = self.grafo.vecinos(nodo_actual, sentido_horario)
            # Imprimimos los vecinos del nodo actual
            print(f"Vecinos del nodo {nodo_actual}: {vecinos}")

            # Para cada vecino
            for vecino in vecinos:
                # Si el vecino no ha sido visitado
                if vecino not in self.visitado:
                    # Calculamos la distancia del vecino al nodo final
                    distancia_vecino = self.grafo.evaluar(vecino, nodo_final)
                    # Si la distancia del vecino es menor que la menor distancia y la distancia del vecino es menor que la distancia del nodo actual al nodo final
                    if distancia_vecino < menor_distancia and distancia_vecino < self.grafo.evaluar(nodo_actual,
                                                                                                    nodo_final):
                        # Actualizamos la menor distancia y el mejor vecino
                        menor_distancia = distancia_vecino
                        mejor_vecino = vecino

            # Si encontramos un mejor vecino
            if mejor_vecino is not None:
                # Agregamos el mejor vecino a los visitados
                self.visitado.add(mejor_vecino)
                # Establecemos el mejor vecino como el nodo actual
                nodo_actual = mejor_vecino
                # Agregamos el nodo actual a la ruta
                self.ruta.append(mejor_vecino)
                # Imprimimos que nos movemos al mejor vecino
                print(f"El nodo {mejor_vecino} es mejor que el nodo actual. Moviendo al nodo {mejor_vecino}.")
            # Si no encontramos un mejor vecino
            else:
                # Imprimimos que no se encontraron mejores vecinos y detenemos la búsqueda
                print("No se encontraron mejores vecinos. Deteniendo la búsqueda.")
                break

        # Devolvemos la ruta
        return self.ruta


# Creamos un grafo y realizamos la búsqueda por escalada maxima pendiente
grafo = grafo.Grafo(grafo.conexiones)
busqueda = BusquedaEscaladaMaximaPendiente(grafo)

# Definimos el nodo inicial, el nodo final y el sentido de la búsqueda
nodo_inicial = '8'
nodo_final = '18'
sentido_horario = True

# Iniciamos la búsqueda desde el nodo inicial hasta el nodo final
print(f"Iniciando la búsqueda desde el nodo {nodo_inicial} hasta el nodo {nodo_final}")
ruta = busqueda.buscar(nodo_inicial, nodo_final, sentido_horario)

# Imprimimos el resultado de la búsqueda por escalada maxima pendiente
print(f"La ruta desde el nodo {nodo_inicial} hasta el nodo {nodo_final} es: {ruta}")
