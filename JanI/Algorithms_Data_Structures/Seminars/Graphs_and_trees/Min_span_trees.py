#!/usr/bin/python3
import sys

from pytokr import pytokr

class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1 
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

item = pytokr()

while True:
    n = int(item())
    m = int(item()) 
    edges = []
    for i in range(m):
        u = int(item())
        v = int(item())
        w = int(item())
        edges.append((u - 1, v - 1, w))  # Subtracting 1 to adjust vertex numbering
    mst_weight = kruskal(edges, n)
    print(mst_weight)  
