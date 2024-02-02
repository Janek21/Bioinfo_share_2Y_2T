import sys

def calculator(tupple):
    if len(tupple) == 1:
        return int(tupple[0])
    else:
        if tupple[0] == '+':
            result = calculator(tupple[1]) + calculator(tupple[2])
        elif tupple[0] == '-':
            result = calculator(tupple[1]) - calculator(tupple[2])
        elif tupple[0] == '*':
            result = calculator(tupple[1]) * calculator(tupple[2])
        elif tupple[0] == '/':
            result = calculator(tupple[1]) / calculator(tupple[2])

        return result


def tree():
    root = sys.stdin.read(1)

        # Check for the end of input
    if root == ' ':
        root = sys.stdin.read(1)


    if root in '1234567890':
        return root
    else:
        return(root, tree(), tree())


tupple = tree()

print(calculator(tupple1))
