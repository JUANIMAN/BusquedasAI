import heapq
import grafo
import distancias_grafo

class Nodo:
    def __init__(self, valor, padre=None):
        self.valor = valor
        self.padre = padre
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, otro):
        return self.valor == otro.valor

    def __lt__(self, otro):
        return self.f < otro.f
    
    def __gt__(self, otro):
        return self.f > otro.f

def a_star(grafo, nodo_inicial, nodo_final):
    nodo_inicial = Nodo(nodo_inicial)
    nodo_final = Nodo(nodo_final)

    lista_abierta = []
    lista_cerrada = []

    heapq.heappush(lista_abierta, nodo_inicial)

    while len(lista_abierta) > 0:
        nodo_actual = heapq.heappop(lista_abierta)
        lista_cerrada.append(nodo_actual)

        if nodo_actual == nodo_final:
            ruta = []
            while nodo_actual != nodo_inicial:
                ruta.append(nodo_actual.valor)
                nodo_actual = nodo_actual.padre
            ruta.append(nodo_inicial.valor)
            return ruta[::-1]

        vecinos = [Nodo(v, nodo_actual) for v in grafo.vecinos(nodo_actual.valor)]

        for vecino in vecinos:
            if vecino in lista_cerrada:
                continue
            vecino.g = nodo_actual.g + distancias_grafo.distancias[nodo_actual.valor][vecino.valor]
            
            if vecino.valor == nodo_final.valor:
                vecino.h = 0
            else:
                vecino.h = distancias_grafo.distancias[vecino.valor][nodo_final.valor]
                
            vecino.f = vecino.g + vecino.h

            if any(nodo_abierto == vecino and vecino.g > nodo_abierto.g for nodo_abierto in lista_abierta):
                continue

            heapq.heappush(lista_abierta, vecino)

    return None

# Crear un grafo y realizar la búsqueda por escalada simple
grafo = grafo.Grafo(grafo.conexiones)

# Definir el nodo inicial, el nodo final y el sentido de la búsqueda
nodo_inicial = '7'
nodo_final = '10'

# Encontrar la ruta usando escalada simple
ruta = a_star(grafo, nodo_inicial, nodo_final)
print(ruta)