import networkx as nx

def read_graph():
    n = int(r())
    m = int(r())
    g = nx.DiGraph()
    g.add_nodes_from(range(n))
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
if init == goal:
    print("yes")
else:
    for e in nx.dfs_edges(g, init):
        if goal == e[1]:
            print("yes")
            break
    else:
        print("no")
