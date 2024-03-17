class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def build_bst(sequence):
    root = None
    for num in sequence:
        root = insert(root, num)
    return root

sequence = []
while True:
    try:
        num = int(input())
        sequence.append(num)
    except EOFError:
        break

root = build_bst(sequence)
preorder_traversal(root)
