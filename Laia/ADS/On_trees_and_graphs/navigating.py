from pytokr import pytokr

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None

def readTree(items, parent=None):
    try:
        data = next(items)
    except StopIteration:
        return None

    if data == '-1':
        return None
    else:
        root = Node(data)
        root.parent = parent
        root.left = readTree(items, root)
        root.right = readTree(items, root)
        return root

def move_tree(root, directions):
    current_node = root

    for direction in directions:
        print(current_node.data)

        if direction == "up" and current_node.parent:
            current_node = current_node.parent
        elif direction == "left" and current_node.left:
            current_node = current_node.left
        elif direction == "right" and current_node.right:
            current_node = current_node.right

    print(current_node.data)

if __name__ == '__main__':
    item, items = pytokr(iter=True)
    n = int(item())

    tree_input = iter(items())
    root = readTree(tree_input)

    # Read the sequence of directions
    directions_input = list(items())

    # Move within the tree according to directions and print content at each step
    move_tree(root, directions_input)