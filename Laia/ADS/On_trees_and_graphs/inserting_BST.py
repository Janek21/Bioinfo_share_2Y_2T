from pytokr import pytokr
item, items = pytokr(iter = True)

def insert_number(number, tree):
    if not tree:
        return (number, None, None)
    else:
        root = tree[0]
        left = tree[1]
        right = tree[2]

        if number < root:
            return (root, insert_number(number, left), right)
        elif number > root:
            return (root, left, insert_number(number, right))
        else:
            return tree

def preordered_tree(tree):
    if tree:
        return [tree[0]] + preordered_tree(tree[1]) + preordered_tree(tree[2])
    return []


numbers = list(items())
tree = None
for number in numbers:
    number = int(number)
    # print(f"reading {number}")
    tree = insert_number(number, tree)
tree = preordered_tree(tree)
for num in tree:
    print(num)
