from pytokr import pytokr
item, items = pytokr(iter = True)

def read_tree_in():
    root = int(item()) # read() returns strings, so we need to transform it inot int
    if root == -1:
        return tuple() # empty trees are represented as empty tuples
    else:
        return (root, read_tree_in(), read_tree_in())

def searching_tree(n, t):
    if not t:
        return False
    elif t[0] == n:
        return True
    elif t[0] > n:
        return searching_tree(n, t[1])
    elif t[0] < n:
        return searching_tree(n, t[2])
    return False


number = int(item())
tree =  read_tree_in()

for number in items():
    n = int(number)
    res = (searching_tree(n, tree))
    if res:
        print(n, end = "")
        print(' ', end = "")
        print(1)
    else:
        print(n, end = "")
        print(' ', end = "")
        print(0)