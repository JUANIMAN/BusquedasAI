import grafo
import distancias_grafo

class escalada_maxima_pendiente:
    def __init__(self, grafo):
        self.grafo = grafo
        self.visitado = set()
        self.ruta = []
        
    def buscar(self, nodo_inicial, nodo_final, sentido_horario=True):
        self._buscar(nodo_inicial, nodo_final, sentido_horario)
        return self.ruta

    def _buscar(self, nodo_inicial, nodo_final, sentido_horario):
        nodo_actual = nodo_inicial
        self.ruta = [nodo_inicial]
        
        while nodo_actual != nodo_final:
            mejor_vecino = None
            for vecino in self.grafo.vecinos(nodo_actual, sentido_horario):
                if vecino == nodo_final:
                    self.ruta.append(vecino)
                    return self.ruta
                if mejor_vecino is None or distancias_grafo.distancias[vecino][nodo_final] < distancias_grafo.distancias[mejor_vecino][nodo_final]:
                    mejor_vecino = vecino
            if mejor_vecino is None or distancias_grafo.distancias[mejor_vecino][nodo_final] >= distancias_grafo.distancias[nodo_actual][nodo_final]:
                return self.ruta
            self.visitado.add(mejor_vecino)
            self.ruta.append(mejor_vecino)
            nodo_actual = mejor_vecino
        return self.ruta

# Crear un grafo y realizar la búsqueda por escalada simple
grafo = grafo.Grafo(grafo.conexiones)
escalada = escalada_maxima_pendiente(grafo)

# Definir el nodo inicial, el nodo final y el sentido de la búsqueda
nodo_inicial = '1'
nodo_final = '28'
sentido_horario = False

# Encontrar la ruta usando escalada simple
ruta = escalada.buscar(nodo_inicial, nodo_final, sentido_horario)
print(ruta)