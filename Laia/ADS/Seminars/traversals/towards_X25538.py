'''
Manually programmed iterative dfs
'''

class MyDiGraph(dict):

    def add_edge(self, u, v):
        self[u].add(v)

    def add_node(self, u):
        self[u] = set()

    def edges(self):
        for u in self:
            for v in self[u]:
                yield u, v, self[u][v]

    def nodes(self):
        for u in self:
            yield u

    def dfs(self, init, goal):
        "search from init for goal node"
        q = list()
        q.append(init)
        seen = set()
        while q:
            curr = q.pop()
            if curr == goal:
                return True
            seen.add(curr)
            for neigh in self[curr]:
                if neigh not in seen:
                    q.append(neigh)
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
print("yes" if g.dfs(init, goal) else "no")
