from pytokr import pytokr
item = pytokr()

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # el parent de cada node s'inicialitza amb ell mateix
        self.rank = [0]*n # al inici tots estan a la mateixa height 

    def find(self, x):
        if self.parent[x] != x: # si el parent d'x no és x
            self.parent[x] = self.find(self.parent[x]) # busca el parent
        return self.parent[x] # retorna'l

    def union(self, x, y): 
        # busca les dues roots
        x_root = self.find(x)
        y_root = self.find(y)

        # si tenen la mateixa root, False <-- cercle
        if x_root == y_root:
            return False

        # segons el rank (height) determina qui és el parent.
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else: # si tenen la mateixa height, s'escull un arbitrariament
            self.parent[y_root] = x_root
            self.rank[x_root] += 1 
        return True # si que es pot unir

def get_weight(edge): 
    return edge[2]

def kruskal(edges, n):
    edges.sort(key = get_weight) # ordernar edges segons el seu weight
    dsu = DisjointSet(n)

    mst_weight = 0
    for edge in edges: # itera pels edges
        u, v, w = edge # agafa els nodes que es conecten i el weight
        if dsu.union(u, v): # mira si es poden unir
            mst_weight += w # s'afegeix el weight
    return mst_weight 


while True:
    n = int(item()) # vertices
    m = int(item()) # edges
    edges = []
    for i in range(m):
        u = int(item())
        v = int(item())
        w = int(item())
        edges.append((u - 1, v - 1, w))  # - 1 to adjust vertex numbering
    mst_weight = kruskal(edges, n)
    print(mst_weight)  
