import networkx as nx

def read_graph():
    n = int(r()) # n vertices
    m = int(r()) # n arcs
    g = nx.DiGraph() # crea el graph
    g.add_nodes_from(range(n)) # crea n nodes
    for _ in range(m): # itera pel n arcs
        u = int(r())
        v = int(r())
        g.add_edge(u, v) # agefeix un edge entre els 2 nodes
    return g


from pytokr import pytokr
r = pytokr()
g = read_graph()
init = int(r()) # valor inicial
goal = int(r()) # valor on vols arribar

if init == goal:
    print("yes")
else:
    for e in nx.dfs_edges(g, init): # passes el graph i la source
        '''
        Llegeix l'arbre tenint com a root (init), i va baixant per cada branca pels edges que pot.
        '''
        if goal == e[1]:
            print("yes")
            break
    else:
        print("no")
