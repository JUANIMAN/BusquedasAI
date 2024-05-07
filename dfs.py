import grafo

class DFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitado = set()
        self.salida = []

    def buscar(self, nodo_inicial, nodo_final, sentido_horario=True):
        self._buscar(nodo_inicial, nodo_final, sentido_horario)
        return self.salida

    def _buscar(self, nodo, nodo_final, sentido_horario):
        if nodo not in self.visitado:
            self.visitado.add(nodo)
            self.salida.append(nodo)
            if nodo == nodo_final:
                return True
            for vecino in self.grafo.vecinos(nodo, sentido_horario):
                if self._buscar(vecino, nodo_final, sentido_horario):
                    return True
        return False

# Crear un grafo y realizar la búsqueda en profundidad
grafo = grafo.Grafo(grafo.conexiones)
dfs = DFS(grafo)

# Definir el nodo inicial, el nodo final y el sentido de la búsqueda
nodo_inicial = '7'
nodo_final = '10'
sentido_horario = False

# Realizar la búsqueda en profundidad
resultado_dfs = dfs.buscar(nodo_inicial, nodo_final, sentido_horario)

# Imprimir el resultado de la búsqueda en profundidad
print("La ruta desde el nodo inicial hasta el nodo final es:", resultado_dfs)
