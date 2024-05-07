class Grafo:
    def __init__(self, conexiones):
        self.conexiones = conexiones

    def vecinos(self, nodo, sentido_horario=True):
        return self.conexiones[nodo] if sentido_horario else self.conexiones[nodo][::-1]

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

# Definir las conexiones
conexiones = {
    '1': ['6', '13', '4'],
    '2': ['22', '12', '9'],
    '3': ['14', '23', '19', '18'],
    '4': ['9', '1', '13'],
    '5': ['15', '11'],
    '6': ['16', '1'],
    '7': ['27', '8', '11'],
    '8': ['27', '15', '7'],
    '9': ['28', '2', '17', '4', '25'],
    '10': ['16', '12'],
    '11': ['7', '5'],
    '12': ['10', '2'],
    '13': ['4', '1', '24'],
    '14': ['23', '3'],
    '15': ['8', '24', '5'],
    '16': ['19', '25', '20', '6', '26', '10'],
    '17': ['26', '9'],
    '18': ['14', '3', '21'],
    '19': ['23', '16', '3'],
    '20': ['25', '16'],
    '21': ['18', '22', '28', '27'],
    '22': ['23', '2', '28', '21'],
    '23': ['14', '19', '22', '3'],
    '24': ['9', '13', '15'],
    '25': [],
    '26': ['16', '17'],
    '27': ['21', '28', '8', '7'],
    '28': ['27', '21', '22', '2', '9', '8']
}

# Crear un grafo y realizar la búsqueda en amplitud
grafo = Grafo(conexiones)
bfs = BFS(grafo)

# Definir el nodo inicial, el nodo final y el sentido de la búsqueda
nodo_inicial = '7'
nodo_final = '10'
sentido_horario = False

# Realizar la búsqueda en amplitud
resultado_bfs = bfs.buscar(nodo_inicial, nodo_final, sentido_horario)

# Imprimir el resultado de la búsqueda en amplitud
print("La ruta desde el nodo inicial hasta el nodo final es:", resultado_bfs)
