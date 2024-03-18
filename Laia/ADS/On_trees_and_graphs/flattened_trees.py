### no

from pytokr import pytokr
read = pytokr()

def calculate_coef(tree):
    def tree_height(tree):
        if not tree:
            return 0
        else:
            children_heights = [tree_height(child) for child in tree[1]]
            return 1 + max(children_heights, default=0)

    def count_nodes(tree):
        if not tree:
            return 0
        else:
            return 1 + sum(count_nodes(child) for child in tree[1])

    h = tree_height(tree)
    s = count_nodes(tree)
    return s / h

def read_tree():
    node = 'X'
    size = int(read())
    children = []
    for _ in range(size):
        children.append(read_tree())
    return [node, children]

def calculate_max_coef(tree):
    if not tree:
        return 0
    
    coef = calculate_coef(tree)
    
    for child in tree[1]:
        coef = max(coef, calculate_max_coef(child))
    
    return coef

n = int(read())

for _ in range(n):
    tree = read_tree()
    coef = calculate_max_coef(tree)
    print('{:.3f}'.format(coef))