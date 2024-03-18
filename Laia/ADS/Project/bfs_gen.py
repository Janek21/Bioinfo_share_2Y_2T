import networkx as nx  # Import NetworkX for efficient graph operations
from collections import deque

class MyDiGraph(nx.DiGraph):

    def __init__(self, incoming=None, edges=None):
        super().__init__(incoming=incoming, edges=edges)  # Call parent constructor

    def bfs(self, init):
        q = deque()
        q.append(init)
        seen = set()
        while q:
            curr = q.popleft()
            seen.add(curr)
            for neigh in self[curr]:
                if neigh not in seen:
                    q.append(neigh)
                    yield
        return False
    

def read_graph():
    n = int(r())
    m = int(r())
    g = MyDiGraph()
    for u in range(n):
        g.add_node(u)
    for _ in range(m):
        u = int(r())
        v = int(r())
        g.add_edge(u, v)
    return g

from pytokr import pytokr
r = pytokr()
g = read_graph()
init = int(r())
goal = int(r())
print("yes" if g.bfs(init) else "no")
