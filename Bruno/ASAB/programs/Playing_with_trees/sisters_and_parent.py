def sisters_and_parent(tree):
    '''
    >>> sisters_and_parent(newick_file2nodes("tree_abcdef.dnd"))
    [(('left', 5, 'B'), ('right', 4, 'A'), ('parent', 3)), (('left', 8, 'D'), ('right', 7, 'C'), ('parent', 6)), (('left', 11, 'F'), ('right', 10, 'E'), ('parent', 9))]
    >>> sisters_and_parent(newick_file2nodes("hmgb.dnd"))
    [(('left', 4, 'hmgl_wheat'), ('right', 3, 'hmgb_chite'), ('parent', 2))]
    '''

    