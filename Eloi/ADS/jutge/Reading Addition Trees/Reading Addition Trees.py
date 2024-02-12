import sys

def tree_reader():
    root=int(read())
    if root==-1:
        return tuple()
    else:
        return(root, tree_reader(), tree_reader())

input_tree = tree_reader()

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

print("pos:", *postorder(input_tree))
print("ino:", *inorder(input_tree))


inp = sys.stdin.readline()

inp = inp.split()
print(inp)
