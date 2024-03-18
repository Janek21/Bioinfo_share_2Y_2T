import networkx as nx

from pytokr import pytokr
r = pytokr()

def read_graph():
    n = int(r())
    m = int(r())
    g = nx.DiGraph()
    g.add_nodes_from(range(n))
    for _ in range(m):
        u = int(r())
        v = int(r())
        weight=int(r())
        g.add_edge(u, v, w=weight)
    return g

def main():

    g = read_graph()
    init = int(r())
    goal = int(r())

    if nx.has_path(g, init, goal):

        minimum_cost=nx.shortest_path_length(g, init, goal, weight="w")
        return minimum_cost
    
    return "no path"

print(main())