from pytokr import pytokr

item = pytokr()

def readtree():
    root = int(item())
    if root == -1:
        return tuple()
    else:
        return (root, readtree(), readtree())


def high(tupple):
     if len(tupple) == 0:
          return 0
     else:
          origin, left, right = tupple
          return max(high(left), high(right)) + 1

n = int(item())

for _ in range(n):
	input = readtree()
	result = high(input)
	print(result)
