
from pytokr import pytokr

read=pytokr()

T = int(read())

def tree_reader(T):
	if T < 0:
		return()
		
	node = int(read()) 
	new_l = int(read())
	
	return (node, tree_reader(new_l-1), tree_reader(T-new_l-1))

input_tree = tree_reader(T-1)

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

print("post:", *postorder(input_tree))
print("in:", *inorder(input_tree))



