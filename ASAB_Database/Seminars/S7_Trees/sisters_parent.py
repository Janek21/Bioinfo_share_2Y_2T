#!/usr/bin/python3

from data.tree_nodes import *

def sisters_and_parent(tree):
    '''
    >>> sisters_and_parent(newick_file2nodes("tree_abcdef.dnd"))
    [(('left', 5, 'B'), ('right', 4, 'A'), ('parent', 3)), (('left', 8, 'D'), ('right', 7, 'C'), ('parent', 6)), (('left', 11, 'F'), ('right', 10, 'E'), ('parent', 9))]
    >>> sisters_and_parent(newick_file2nodes("hmgb.dnd"))
    [(('left', 4, 'hmgl_wheat'), ('right', 3, 'hmgb_chite'), ('parent', 2))]
    '''
    ls=[]
    for key in tree:

        node=str(tree[key])
        
        if node.endswith("_"): #is it a leaf? we want non-leaf nodes

            lf=tree[key].left #define left and right position
            rg=tree[key].right
            
            left=("left", lf, tree[lf]) #define left and right tuple
            right=("right", rg, tree[rg]) ##str(tree[lf]).replace("node_", "") the third argument as the name of the leaf without node_?
            
            if str(left[2])!="node_" and str(right[2])!="node_": #check that left and right nodes are leafs

                parent=("parent", key) #define as parent the current node (parent of left and right)
                combo4key=(left, right, parent)
                ls.append(combo4key)

    return(ls)

#print(sisters_and_parent(newick_file2nodes("tree_abcdef.dnd")))

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)