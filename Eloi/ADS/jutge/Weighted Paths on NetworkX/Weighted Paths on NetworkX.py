import networkx as nx

# Read input
n, m = map(int, input().split())

# Create directed graph
G = nx.DiGraph()

# Add weighted arcs
for _ in range(m):
    u, v, w = map(int, input().split())
    G.add_edge(u, v, weight=w)

# Read x and y
x, y = map(int, input().split())

# Find shortest path
try:
    shortest_path_cost = nx.shortest_path_length(G, source=x, target=y, weight='weight')
    print(shortest_path_cost)
except nx.NetworkXNoPath:
    print("no path")
