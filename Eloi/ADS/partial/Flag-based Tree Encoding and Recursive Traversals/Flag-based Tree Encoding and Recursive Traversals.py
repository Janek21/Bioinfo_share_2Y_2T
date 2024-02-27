from pytokr import pytokr

inp=pytokr()


def tree_reader(T):
	if T == -1: #Check if path is empty
		return()
		
	node = int(inp()) # Take Node
	left = int(inp()) # Take left indicator
	right = int(inp()) #Take Right indicator
	
	return (node, tree_reader(left), tree_reader(right))

input_tree = tree_reader(1) # Initiate reading

def postorder(input_tree): # Traverse in postorder
	if not input_tree:
		return []
	left = postorder(input_tree[1])
	right = postorder(input_tree[2])
	return left + right + [input_tree[0]]


def inorder(input_tree): # Traverse in inorder
	if not input_tree:
		return []
	left = inorder(input_tree[1])
	right = inorder(input_tree[2])
	return left + [input_tree[0]] + right

print("post:", *postorder(input_tree))
print("in:", *inorder(input_tree))



