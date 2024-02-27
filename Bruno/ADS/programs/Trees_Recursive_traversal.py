from pytokr import pytokr

item = pytokr()

def readtree():
    root = int(item())
    if root == -1:
        return tuple()
    else:
        return (root, readtree(), readtree())

s = readtree()

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

#print(s)
postorder_result = postorder(s)
inorder_result = inorder(s)


print("pos:", " ".join(map(str, postorder_result)))
print("ino:", " ".join(map(str, inorder_result)))
