from pytokr import pytokr

s = pytokr()

def readtree():
    root = int(s())
    if root == -1:
        return tuple()
    else:
        return (root, readtree(), readtree())

input_tree = readtree()

def postorder(input_tree):
    if not input_tree:
        return []
    left = postorder(input_tree[1])
    right = postorder(input_tree[2])
    return left + right + [input_tree[0]]

def inorder(input_tree):
    if not input_tree:
        return []
    left = inorder(input_tree[1])
    right = inorder(input_tree[2])
    return left + [input_tree[0]] + right


postorder_result = postorder(input_tree)
inorder_result = inorder(input_tree)


print("pos:", " ".join(map(str, postorder_result)))
print("ino:", " ".join(map(str, inorder_result)))
