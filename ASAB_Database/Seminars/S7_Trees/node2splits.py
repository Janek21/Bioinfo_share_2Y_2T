# Figure out how to to print *leaves*. A *leaf* is a node with no descendants.

from tree_nodes import *


def node2splits(i_node, nodes):
    # sourcery skip: extract-method, inline-immediately-returned-variable, remove-unnecessary-else, swap-if-else-branches
    """This function should call itself in a recursive way. The idea is to start
    exploring left then rigth - or the other way around. Takes as input the node id to start
    the recursion, a dictionary of nodes and the list of leaves which initially should be emtpy.
    >>> node2splits(1, newick_file2nodes("tree_abcdef.dnd"))
    ['F'] ['E']
    ['D'] ['C']
    ['B'] ['A']
    ['D', 'C'] ['B', 'A']
    ['F', 'E'] ['D', 'C', 'B', 'A']
    ['F', 'E', 'D', 'C', 'B', 'A']
    >>> node2splits(1, newick_file2nodes("hmgb.dnd"))
    ['hmgl_wheat'] ['hmgb_chite']
    ['hmgl_trybr'] ['hmgl_wheat', 'hmgb_chite']
    ['hmgt_mouse'] ['hmgl_trybr', 'hmgl_wheat', 'hmgb_chite']
    ['hmgt_mouse', 'hmgl_trybr', 'hmgl_wheat', 'hmgb_chite']
    """
    if nodes[i_node].left == 0 or nodes[i_node].right == 0:
        return [nodes[i_node].name]
    else:
        # accumulate sepparately for left and right
        left_list = node2splits(nodes[i_node].left, nodes)
        right_list = node2splits(nodes[i_node].right, nodes)
        print(left_list, right_list)
        return left_list + right_list

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)