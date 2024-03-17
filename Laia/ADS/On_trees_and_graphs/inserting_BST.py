class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def preorder_traversal(root):
    if root:
        print(root.key)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def build_bst(sequence):
    root = None
    for num in sequence:
        root = insert(root, num)
    return root

if __name__ == "__main__":
    sequence = []
    while True:
        try:
            num = int(input())
            sequence.append(num)
        except EOFError:
            break
    
    root = build_bst(sequence)
    preorder_traversal(root)
