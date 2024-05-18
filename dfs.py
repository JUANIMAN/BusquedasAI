# Importamos la clase Grafo
import grafo


# Definimos la clase DFS para la búsqueda en profundidad
class DFS:
    # Inicializamos la clase con el grafo, un conjunto para los nodos visitados y un diccionario para los padres de los nodos
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitado = set()
        self.padres = {}

    # Método para realizar la búsqueda
    def buscar(self, nodo_inicial, nodo_final, sentido_horario=True):
        # Inicializamos la pila con el nodo inicial
        pila = [nodo_inicial]

        # Mientras la pila no esté vacía
        while pila:
            # Sacamos el último nodo de la pila
            nodo_actual = pila.pop()
            print(f"Visitando el nodo: {nodo_actual}")

            # Si el nodo es el nodo final, detenemos la búsqueda y devolvemos la ruta
            if nodo_actual == nodo_final:
                return self._ruta(nodo_actual)

            # Si el nodo no ha sido visitado, lo marcamos como visitado y agregamos sus vecinos a la pila
            if nodo_actual not in self.visitado:
                self.visitado.add(nodo_actual)
                vecinos = self.grafo.vecinos(nodo_actual, sentido_horario)
                print(f"Vecinos del nodo {nodo_actual}: {vecinos}")

                # Se invierte el sentido para su correcta revisión en la pila
                vecinos = vecinos[::-1]

                for vecino in vecinos:
                    if vecino not in self.visitado:
                        self.padres[vecino] = nodo_actual
                        pila.append(vecino)
                        print(f"Agregando el nodo {vecino} a la pila")

    # Método para construir la ruta desde el nodo inicial hasta el nodo actual
    def _ruta(self, nodo_actual):
        ruta = []
        while nodo_actual != nodo_inicial:
            ruta.append(nodo_actual)
            nodo_actual = self.padres[nodo_actual]
        ruta.append(nodo_inicial)
        return ruta[::-1]  # Devolvemos la ruta en orden inverso


# Creamos un grafo y realizamos la búsqueda en profundidad
grafo = grafo.Grafo(grafo.conexiones)
dfs = DFS(grafo)

# Definimos el nodo inicial, el nodo final y el sentido de la búsqueda
nodo_inicial = '8'
nodo_final = '18'
sentido_horario = True

# Realizamos la búsqueda en profundidad
print(f"Iniciando la búsqueda desde el nodo {nodo_inicial} hasta el nodo {nodo_final}")
resultado_dfs = dfs.buscar(nodo_inicial, nodo_final, sentido_horario)

# Imprimimos el resultado de la búsqueda en profundidad
print(f"La ruta desde el nodo {nodo_inicial} hasta el nodo {nodo_final} es: {resultado_dfs}")
