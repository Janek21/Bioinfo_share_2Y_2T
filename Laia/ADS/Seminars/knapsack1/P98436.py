from pytokr import pytokr

def postorder(tree):
    if tree:
        r = postorder(tree[1])
        r.extend(postorder(tree[2]))
        r.append(tree[0])
        return r
    else:
        return list()


def inorder(tree):
    if tree:
        r = inorder(tree[1])
        r.append(tree[0])
        r.extend(inorder(tree[2]))
        return r
    else:
        return list()

def read_tree_in(readitem):
    item = int(readitem())
    if item == -1:
        return tuple()
    else:
        return (item, read_tree_in(readitem), read_tree_in(readitem))

# Careful: in P98436, different from P57669, there is no size to ignore

readitem = pytokr()

t = read_tree_in(readitem)

# ~ print("pos:", " ".join(map(str, postorder(t)))) # PE in P98436
# ~ print("ino:", " ".join(map(str, inorder(t))))

print("pos:", end = '')
for item in postorder(t):
    print(' ' + str(item), end = '')
print()
print("ino:", end = '')
for item in inorder(t):
    print(' ' + str(item), end = '')
print()
