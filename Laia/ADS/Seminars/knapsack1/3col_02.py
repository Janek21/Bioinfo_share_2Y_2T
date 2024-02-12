"""
Edge-coloring a (3-regular?) graph by backtracking - not particularly smart one

Jose L Balcazar, 2023, 2024, laboriously adapted to NetworkX 3.0 and Python 3 and PyGraphViz
"""

import networkx as nx
from matplotlib import pyplot as plt

k = 3 # number of available colors, max 5 for the time being
draw_dead_ends = True

five_colors = [ 'r', 'g', 'b', 'm', 'c' ]
colors = five_colors[:k]
noncolor = 'k' # black: default color of graph drawing software

def triang_3_wheel():
	"""
	Constructs a specific 3-regular graph on 10 vertices
	"""
	G = nx.Graph()
	G.add_edges_from( [ (0, 1), (0, 2), (1, 2),
						(3, 4), (3, 5), (4, 5), (4, 0),
						(6, 7), (6, 8), (7, 8), (6, 1), (7, 3),
						(2, 9), (5, 9), (8, 9) ] )
	return G

def drawgraph(g, gd, marked = None):
	"""
	drawing the current graph, 
	possibly with a marked edge that
	does not allow for coloring 
	"""
	nx.draw_networkx_nodes(g, gd)
	nx.draw_networkx_labels(g, gd)
	for (u, v) in g.edges():
		"one by one due to the different colors"
		w = 3
		if marked == (u, v) or marked == (v, u):
			"thicker marked edge"
			w = 8
			print("No color available for", marked, '.')
		c = g.edges[u, v].get('color', noncolor) # edge color if exists, o/w default black
		nx.draw_networkx_edges(g, gd, edgelist = [(u, v)], width = w, edge_color = c)
	plt.show()

def edgecolor(g, gd, edgelist):
	"""
	Edgelist handled as a stack: pop next edge, color it in all
	possible ways ( = free colors at both endpoints) and, for each 
	color, recurse on the rest of the list; if no solution found, 
	push the edge back in for the backtracking step.
	Report just first solution found.
	Layout transmitted in dict gd, contains vertex coordinates.
	"""
	if not edgelist:
		"empty list: successful exploration, we are done"
		print("No pending edges.")
		return True
	else:
		print("Currently pending edges:", end = ' ')
		for e in edgelist: print(e, end = ' ')
		print('.')
		u, v = edgelist.pop()
		possib = g.nodes[u]['free'] & g.nodes[v]['free'] # set intersection
		if len(possib) == 0 and draw_dead_ends:
			"no color available for this edge, report that"
			drawgraph(g, gd, marked = (u, v))
		for c in possib:
			g.edges[u, v]['color'] = c
			g.nodes[u]['free'].remove(c)
			g.nodes[v]['free'].remove(c)
			success = edgecolor(g, gd, edgelist)
			if success:
				"transmit success back to finish all pending recursive calls"
				return True
			# else, free again the colors to try the next possib
			g.edges[u, v]['color'] = noncolor
			g.nodes[u]['free'].add(c)
			g.nodes[v]['free'].add(c)
		edgelist.append((u, v)) # all possib tried and failed, backtrack
		return False

if __name__ == "__main__":

	# ~ g = triang_3_wheel()    # one specific 3-regular, 3-colorable size 10 graph

	# ~ g = nx.random_regular_graph(k, 10) # for k = 3, almost all are 3-colorable

	g = nx.petersen_graph() # 3-regular, 4-colorable, not 3-colorable,  
                                # might show up also from a random_regular()
                                # call, but very infrequently: see
                                # https://en.wikipedia.org/wiki/Petersen_graph

	for n in g.nodes():
		"initially, all colors available everywhere"
		g.nodes[n]['free'] = set(colors)

	gd = nx.nx_agraph.graphviz_layout(g, prog = "fdp") # needs pygraphviz
	
	print(list(set(colors)))

	edgelist = list(nx.edge_dfs(g))
	edgelist = list(reversed(edgelist))
	drawgraph(g, gd)

	success = edgecolor(g, gd, edgelist) # start backtracking

	if not success:
		print("No 3-coloring possible.")
	else:
		print("Success in 3-coloring graph.")
		drawgraph(g, gd)


