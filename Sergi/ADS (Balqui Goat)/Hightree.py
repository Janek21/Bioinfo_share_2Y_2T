from pytokr import pytokr

s = pytokr()

def readtree():
    root_value = int(s())
    if root_value == -1:
        return None
    else:
        left_subtree = readtree()
        right_subtree = readtree()
        return (root_value, left_subtree, right_subtree)

def tree_height(root):
    if root is None:
        return 0
    _, left_height, right_height = root
    return max(tree_height(left_height), tree_height(right_height)) + 1

m = int(s())

for _ in range(m):
    input_tree = readtree()
    height = tree_height(input_tree)
    print(height)



