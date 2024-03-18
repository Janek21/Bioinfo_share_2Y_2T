'''
Minimum spanning trees via hand-coded Kruskal

NOTE: The statement allows for parallel edges
'''

from pytokr import item, items
from heapq import heapify, heappop

class MyUF(dict):
	
	def new(self, x):
		self[x] = x
	
	def find(self, v):
		if v == self[v]:
			return v
		r = self.find(self[v])
		self[v] = r           # path compression
		return r
		
	def union(self, x, y):
		xx = self.find(x)
		yy = self.find(y)
		self[xx] = yy

class MyGraph(dict):
	
	def add_edge(self, u, v, w):
		assert u != v
		u, v = min(u, v), max(u, v) # store undirected edge in this direction
		if u not in self:
			self[u] = dict()
		if v not in self:
			self[v] = dict()
		if v not in self[u]:
			self[u][v] = float("inf")
		self[u][v] = min(self[u][v], w) # in case of parallel edges: keep cheapest

	def edges(self):
		for u in self:
			for v in self[u]:
				yield u, v, self[u][v]

	def nodes(self):
		for u in self:
			yield u

def kruskal(g):
	uf = MyUF()
	for u in g.nodes():
		uf.new(u)
	h = list()
	for u, v, w in g.edges():
		h.append((w, u, v))
	heapify(h)
	mst = MyGraph()
	mst_edges = 0
	cost = 0
	while mst_edges < len(g) - 1 and h:
		w, u, v = heappop(h)
		if uf.find(u) != uf.find(v):
			mst.add_edge(u, v, w)
			mst_edges += 1
			cost += w
			uf.union(u, v)
	return mst, cost


for size in items():
	g = MyGraph()
	size = int(size)
	edges = int(item())
	for _ in range(edges):
		u, v, w = int(item()), int(item()), int(item())
		g.add_edge(u, v, w)
	# ~ for u, v, w in g.edges():
		# ~ print(u, v, g[u][v], w)
	st, cost = kruskal(g) 
	print(cost)
	# ~ for u, v, w in st.edges():
		# ~ print(u, v, st[u][v], w)



