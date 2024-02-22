class DisjointSet:

    def __init__(self, n):
    
        self.parent = [i for i in range(n)]  # Initialize parent array 
        self.rank = [0] * n  # Initialize rank array with all zeros

    def find(self, x):
    
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]  # Return the root node

    def union(self, x, y):
        
        x_root = self.find(x)  # root of node x
        y_root = self.find(y)  #root of node y

        if x_root == y_root:
            return False  

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root  # Set the parent of x's root to y's root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root  # Set the parent of y's root to x's root
        else:
            self.parent[y_root] = x_root  # Set the parent of y's root to x's root
            self.rank[x_root] += 1  # Increase rank of x's root

        return True 

def get_weight(edge):
    return edge[2]

def kruskal(edges, n):
    edges.sort(key=get_weight)
    dsu = DisjointSet(n)
    
    mst_weight = 0
    
    for edge in edges:
        u, v, w = edge
        if dsu.union(u, v):
            mst_weight += w  # Add weight of the current edge to MST if it's added

    return mst_weight 

while True:
    try:
        n, m = map(int, input().split())  
        edges = []
        for i in range(m):
            u, v, w = map(int, input().split())
            edges.append((u - 1, v - 1, w))  # Subtracting 1 to adjust vertex numbering
        mst_weight = kruskal(edges, n)
        print(mst_weight)  
    except EOFError:
        break  
