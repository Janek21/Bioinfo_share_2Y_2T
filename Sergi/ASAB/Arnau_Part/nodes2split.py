from tree_nodes import *


def node2splits(node_id, nodes):
    '''
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
  
    '''

 
    node = nodes[node_id]


    left_list = []
    right_list = []

    if node.left == 0 and node.right == 0:
        return [node.name]

    # Left
    if node.left != 0:
        left_list = node2splits(node.left, nodes)

    # Right
    if node.right != 0:
        right_list = node2splits(node.right, nodes)

    # Print left and right lists
    print(left_list, right_list)

    return left_list + right_list



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
