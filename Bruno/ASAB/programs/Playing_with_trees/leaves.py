import os
working_dir = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/Playing_with_trees'

os.chdir(working_dir)

from tree_nodes import *

def leaves(nodes):
    '''
    >>> leaves(newick_file2nodes("tree_abcdef.dnd"))
    [(4, 'A'), (5, 'B'), (7, 'C'), (8, 'D'), (10, 'E'), (11, 'F')]
    >>> leaves(newick_file2nodes("hmgb.dnd"))
    [(3, 'hmgb_chite'), (4, 'hmgl_wheat'), (5, 'hmgl_trybr'), (7, 'hmgt_mouse')]
    '''
    leaf_nodes = []
    for node_id, node in nodes.items(): #Iterate through each pair of nodes 
        if node.left == 0 and node.right == 0:
            leaf_nodes.append((node_id, node.name))
    return leaf_nodes



if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)