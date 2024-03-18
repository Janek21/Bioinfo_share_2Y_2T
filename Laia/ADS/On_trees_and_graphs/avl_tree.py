class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if node is None:
            return 0
        return node.height
    
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        
        return x
    
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        return y
    
    def insert(self, node, key):
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        
        balance = self.balance(node)
        
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)
    
    def insert_list(self, arr):
        for key in arr:
            self.root = self.insert(self.root, key)

# Test the AVL tree with a list of numbers
if __name__ == "__main__":
    avl_tree = AVLTree()
    numbers = [10, 5, 15, 3, 7, 12, 17]

    avl_tree.insert_list(numbers)

    print("Inorder Traversal of constructed AVL tree is:")
    avl_tree.inorder_traversal(avl_tree.root)
