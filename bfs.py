import grafo

class BFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitado = set()
        self.salida = []
    
    def buscar(self, nodo_inicial, nodo_final, sentido_horario=True):
        self._buscar(nodo_inicial, nodo_final, sentido_horario)
        return self.salida

    def _buscar(self, nodo_inicial, nodo_final, sentido_horario):
        cola = [nodo_inicial]

        while cola:
            nodo = cola.pop(0)
            if nodo not in self.visitado:
                self.visitado.add(nodo)
                self.salida.append(nodo)

                # Si el nodo es el nodo final, detener la búsqueda
                if nodo == nodo_final:
                    return self.salida

                # Agregar todos los nodos adyacentes no visitados a la cola
                for vecino in self.grafo.vecinos(nodo, sentido_horario):
                    if vecino not in self.visitado:
                        cola.append(vecino)

        return self.salida


# Crear un grafo y realizar la búsqueda en amplitud
grafo = grafo.Grafo(grafo.conexiones)
bfs = BFS(grafo)

# Definir el nodo inicial, el nodo final y el sentido de la búsqueda
nodo_inicial = '7'
nodo_final = '10'
sentido_horario = False

# Realizar la búsqueda en amplitud
resultado_bfs = bfs.buscar(nodo_inicial, nodo_final, sentido_horario)

# Imprimir el resultado de la búsqueda en amplitud
print("La ruta desde el nodo inicial hasta el nodo final es:", resultado_bfs)
