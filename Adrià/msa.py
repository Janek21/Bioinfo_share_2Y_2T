from tree_nodes import *
from fasta2dict import fasta2dict
from align_profiles_names import align_profiles



def node2splits_align(node_id, nodes,dic,gep):
    '''
    >>> node2splits_align(1, newick_file2nodes("hmgb.dnd"), fasta2dict("hmgb.fasta"), -4)
    ['hmgt_mouse', 'hmgl_trybr', 'hmgl_wheat', 'hmgb_chite']
    >>> node2splits_align(2, newick_file2nodes("hmgb.dnd"), fasta2dict("hmgb.fasta"), -4)
    ['hmgl_wheat', 'hmgb_chite']
    >>> node2splits_align(6, newick_file2nodes("hmgb.dnd"), fasta2dict("hmgb.fasta"), -4)
    ['hmgl_trybr', 'hmgl_wheat', 'hmgb_chite']
    '''
 
    node = nodes[node_id]


    left_list = []
    right_list = []

    if node.left == 0 and node.right == 0:
        return [node.name]

    # Left
    if node.left != 0:
        left_list = node2splits_align(node.left, nodes,dic, gep)

    # Right
    if node.right != 0:
        right_list = node2splits_align(node.right, nodes,dic, gep)

    align_profiles(dic, left_list, right_list, gep)
    return left_list + right_list



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)