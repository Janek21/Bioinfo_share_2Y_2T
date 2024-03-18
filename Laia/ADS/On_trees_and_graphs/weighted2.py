from pytokr import pytokr
import networkx as nx
import heapq
r = pytokr()

def read_input():
    n = int(r())
    m = int(r())
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    for _ in range(m):
        u, v, weight = int(r()), int(r()), int(r())
        G.add_edge(u, v, weight=weight)
    return G

def dijkstra(G, source):
    # Inicializa un diccionario para almacenar las distancias mínimas de cada nodo desde el nodo origen.
    distances = {node: float('inf') for node in G.nodes}
    # Establece la distancia del nodo origen a sí mismo como 0.
    distances[source] = 0
    # Inicializa una cola de prioridad (heap) con la distancia del nodo origen a sí mismo.
    heap = [(0, source)]
    # Mientras haya elementos en el heap:
    while heap:
        # Extrae el nodo con la menor distancia actual desde el origen.
        current_distance, current_node = heapq.heappop(heap)
        # Si la distancia extraída es mayor que la distancia almacenada, continúa al siguiente nodo.
        if current_distance > distances[current_node]: # com és més gran, no l'utilitzarem
            continue
        # Explora los vecinos del nodo actual.
        for neighbor, weight in G[current_node].items():
            # Calcula la distancia desde el origen al vecino a través del nodo actual.
            distance = current_distance + weight['weight']
            # Si la nueva distancia es menor que la distancia almacenada previamente,
            # actualiza la distancia mínima y agrega el vecino al heap.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    # Devuelve el diccionario de distancias mínimas desde el nodo origen.
    return distances


G = read_input()
x = int(r())
y = int(r())

distances = dijkstra(G, x)

if distances[y] != float('inf'):
    print(distances[y])
else:
    print("no path")
