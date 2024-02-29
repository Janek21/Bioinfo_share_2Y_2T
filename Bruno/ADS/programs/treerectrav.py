from pytokr import pytokr

item = pytokr()

def read_tree():
    root = int(item())

    if root == -1:
        return tuple()

    else:
        return (root, read_tree(), read_tree())



def postorder(tupple):
    if len(tupple) == 0:
        return []
    else:
        left = postorder(tupple[1])
        right = postorder(tupple[2])
        return left + right + [tupple[0]]
    


tupple = read_tree()

post = postorder(tupple)
#print(post)

a = ' '.join(map(str, post))
#print(a)

def inorder(tupple):
    if len(tupple) == 0:
        return []
    else:
        left = inorder(tupple[1])
        rigth = inorder(tupple[2])
        return left + [tupple[0]] + rigth

inord = inorder(tupple)

b = ' '.join(map(str, inord))
#print(b)


print(f'pos: {a}')
print(f'ino: {b}')