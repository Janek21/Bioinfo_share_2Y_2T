from tree_nodes import *


def node2leaves(node_id, nodes, leaves_list):

    '''
    >>> node2leaves(1, newick_file2nodes("tree_abcdef.dnd"), [])
    ['F', 'E', 'D', 'C', 'B', 'A']
    >>> node2leaves(2, newick_file2nodes("tree_abcdef.dnd"), [])
    ['D', 'C', 'B', 'A']
    >>> node2leaves(3, newick_file2nodes("tree_abcdef.dnd"), [])
    ['B', 'A']
    >>> node2leaves(4, newick_file2nodes("tree_abcdef.dnd"), [])
    ['A']
    >>> node2leaves(5, newick_file2nodes("tree_abcdef.dnd"), [])
    ['B']
    >>> node2leaves(6, newick_file2nodes("tree_abcdef.dnd"), [])
    ['D', 'C']
    >>> node2leaves(7, newick_file2nodes("tree_abcdef.dnd"), [])
    ['C']
    >>> node2leaves(8, newick_file2nodes("tree_abcdef.dnd"), [])
    ['D']
    >>> node2leaves(9, newick_file2nodes("tree_abcdef.dnd"), [])
    ['F', 'E']
    >>> node2leaves(10, newick_file2nodes("tree_abcdef.dnd"), [])
    ['E']
    >>> node2leaves(11, newick_file2nodes("tree_abcdef.dnd"), [])
    ['F']
    >>> node2leaves(1, newick_file2nodes("hmgb.dnd"), [])
    ['hmgt_mouse', 'hmgl_trybr', 'hmgl_wheat', 'hmgb_chite']
    >>> node2leaves(2, newick_file2nodes("hmgb.dnd"), [])
    ['hmgl_wheat', 'hmgb_chite']
    >>> node2leaves(3, newick_file2nodes("hmgb.dnd"), [])
    ['hmgb_chite']
    >>> node2leaves(4, newick_file2nodes("hmgb.dnd"), [])
    ['hmgl_wheat']
    >>> node2leaves(5, newick_file2nodes("hmgb.dnd"), [])
    ['hmgl_trybr']
    >>> node2leaves(6, newick_file2nodes("hmgb.dnd"), [])
    ['hmgl_trybr', 'hmgl_wheat', 'hmgb_chite']
    >>> node2leaves(7, newick_file2nodes("hmgb.dnd"), [])
    ['hmgt_mouse']
    '''
 
    
    node = nodes[node_id]

    # If the current node is a leaf, append its name to the leaves_list
    if node.left == 0 and node.right == 0:
        leaves_list.append(node.name)
    else:
        # Left
        if node.left != 0:
            node2leaves(node.left, nodes, leaves_list)
        # Right
        if node.right != 0:
            node2leaves(node.right, nodes, leaves_list)

    return leaves_list


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


