from pytokr import pytokr
item = pytokr()


def read_tree():
    node = int(item())
    child = int(item())
    children = list()
    for _ in range(child):
        children.append(read_tree())
    return[node, children]

def postorder(tree):
    if not tree:
        return []
    result = []
    for child in tree[1]: 
        result.extend(postorder(child))
    result.append(tree[0])  
    return result

c = int(item())
tree = read_tree()
res = postorder(tree)

print('',*res)
    


