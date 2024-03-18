#!/usr/bin/python3
from pytokr import pytokr
import sys
item = pytokr()

class Node:
    def __init__(self, data):
        self.esquerra = None
        self.dreta = None
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
        root.esquerra = readTree(items, root)
        root.dreta = readTree(items, root)
        return root

def move_tree(root, directions):
    current_node = root

    for direction in directions:
        print(current_node.data)

        if direction == "amunt" and current_node.parent:
            current_node = current_node.parent
        elif direction == "esquerra" and current_node.esquerra:
            current_node = current_node.esquerra
        elif direction == "dreta" and current_node.dreta:
            current_node = current_node.dreta

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