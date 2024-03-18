from pytokr import pytokr

item = pytokr()

def tree():
    root = item()
    if root != '+':
        root = float(root)
    if isinstance(root, float):
        return float(root)
    else:
        return[root, tree(), tree()]
    

def eval_tree(tree):
    if isinstance(tree, float):
        return tree
    else:
        subtree1 = eval_tree(tree[1])
        left = subtree1
        subtree2 = eval_tree(tree[2])
        right = subtree2
        tree[0] = left+right
        return tree[0]
        
def preorder(tree):
    if isinstance(tree, float):
        return [tree]
    elif isinstance(tree, list):
        result = []
        for item in tree:
            result += preorder(item)
        return result
    else:
        return []

def postorder(tree):
    if isinstance(tree, float):
        return [tree]
    else:
        left = postorder(tree[1])
        right = postorder(tree[2])
        return left + right + [tree[0]]

def inorder(tree):
    if isinstance(tree, float):
        return [tree]
    else:
        left = inorder(tree[1])
        right = inorder(tree[2])
        return left + [tree[0]] + right



input = tree()
eval_tree(input)
pre = preorder(input)
for item in range(len(pre)):
    pre[item] = '{:.4f}'.format(pre[item])
post = postorder(input)
for item in range(len(post)):
    post[item] = '{:.4f}'.format(post[item])
ino = inorder(input)
for item in range(len(ino)):
    ino[item] = '{:.4f}'.format(ino[item])


print(*pre,'')
print(*ino,'')
print(*post,'')