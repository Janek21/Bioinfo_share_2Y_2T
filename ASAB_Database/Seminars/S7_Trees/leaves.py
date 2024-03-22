#!/usr/bin/python3

from Bio import Phylo
from io import StringIO
from data.tree_nodes import *
#newick_file2nodes is modified by adding
#newick_file="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S7_Trees/data/"+newick_file


def leaves(tree):
    '''
    >>> leaves(newick_file2nodes("tree_abcdef.dnd"))
    [(4, 'A'), (5, 'B'), (7, 'C'), (8, 'D'), (10, 'E'), (11, 'F')]
    >>> leaves(newick_file2nodes("hmgb.dnd"))
    [(3, 'hmgb_chite'), (4, 'hmgl_wheat'), (5, 'hmgl_trybr'), (7, 'hmgt_mouse')]
    '''
    ls=[]
    for key in tree:

        node=str(tree[key])

        if not node.endswith("_"): #nodes that dont end in _ end in a letter, they are leaves
            ls.append((key,  node.replace("node_", ""))) #add to ls key(number), land all letters of node that are not node_ (the leaf)

    return ls

if __name__ == "__main__":

	import doctest
	doctest.testmod(verbose=True)