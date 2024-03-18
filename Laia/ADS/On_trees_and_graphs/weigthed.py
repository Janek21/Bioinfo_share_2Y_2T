from pytokr import pytokr
import networkx as nx
r = pytokr()

def read_input():
    n = int(r())
    m = int(r())
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    for _ in range(m):
        G.add_edge(int(r()), int(r()), weight=int(r()))
    return G

G = read_input()
x = int(r())
y = int(r())

if nx.has_path(G, source=x, target=y): # busca si hi ha path entre x i y.
    min_cost = nx.shortest_path_length(G, source=x, target=y, weight='weight') # calcula el cost del shortest path.
    print(min_cost)
else:
    print("no path") 