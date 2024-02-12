from pytokr import pytokr
item = pytokr()

def read_input():
    root = int(item())
    if root == -1:
        return tuple()
    else:
        return (root, read_input(), read_input())

def heigth(tree):
    if not tree:
        return 0
    else:
        left = heigth(tree[1]) + 1
        right = heigth(tree[2]) + 1
        return max(left, right)

n = int(item())
for x in range(n):
    inp = read_input()
    print(heigth(inp))