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


def takeinput():
    root = sys.stdin.read(1)

        # Check for the end of input
    if root == ' ':
        root = sys.stdin.read(1)


    if root in '1234567890':
        return root
    else:
        return(root, tree(), tree())

tupple1 = takeinput()

print(calculator(tupple1))













#tupple2 = ['+', '4', '3']
#tupple3 =['*', '8', ['+', '4', '3']]
#tupple4 = ['*', ['-', '2', '8'], ['+', '4', '3']]


#print(calculator(tupple2))
#print(calculator(tupple3))
#print(calculator(tupple4))

#print(tree())
