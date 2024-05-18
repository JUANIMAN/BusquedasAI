# Importamos la clase Grafo
import grafo


# Definimos la clase BusquedaEscaladaSimple
class BusquedaEscaladaSimple:
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
            # Obtenemos los vecinos del nodo actual
            vecinos = self.grafo.vecinos(nodo_actual, sentido_horario)
            # Imprimimos los vecinos del nodo actual
            print(f"Vecinos del nodo {nodo_actual}: {vecinos}")

            # Para cada vecino
            for vecino in vecinos:
                # Si el vecino no ha sido visitado y su evaluación es menor que la del nodo actual
                if vecino not in self.visitado and self.grafo.evaluar(vecino, nodo_final) < self.grafo.evaluar(
                        nodo_actual, nodo_final):
                    # Agregamos el vecino a los visitados
                    self.visitado.add(vecino)
                    # Establecemos el vecino como el nodo actual
                    nodo_actual = vecino
                    # Agregamos el nodo actual a la ruta
                    self.ruta.append(vecino)
                    # Imprimimos que nos movemos al vecino
                    print(f"El nodo {vecino} es mejor que el nodo actual. Moviendo al nodo {vecino}.")
                    # Rompemos el ciclo for
                    break
            # Si no se encontraron mejores vecinos
            else:
                # Imprimimos que no se encontraron mejores vecinos y detenemos la búsqueda
                print("No se encontraron mejores vecinos. Deteniendo la búsqueda.")
                break

        # Devolvemos la ruta
        return self.ruta


# Creamos un grafo y realizamos la búsqueda por escalada simple
grafo = grafo.Grafo()
busqueda = BusquedaEscaladaSimple(grafo)

# Definimos el nodo inicial, el nodo final y el sentido de la búsqueda
nodo_inicial = '8'
nodo_final = '18'
sentido_horario = True

# Iniciamos la búsqueda desde el nodo inicial hasta el nodo final
print(f"Iniciando la búsqueda desde el nodo {nodo_inicial} hasta el nodo {nodo_final}")
ruta = busqueda.buscar(nodo_inicial, nodo_final, sentido_horario)

# Imprimimos el resultado de la búsqueda por escalada simple
print(f"La ruta desde el nodo {nodo_inicial} hasta el nodo {nodo_final} es: {ruta}")
