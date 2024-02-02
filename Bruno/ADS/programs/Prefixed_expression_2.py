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

def take_input(line_list):
    operation = []
    binomio = []
    binomio.append(line_list[0])
    line_list[0].pop()


def tree():
    root = sys.stdin.read(1)

        # Check for the end of input
    if root == ' ':
        root = sys.stdin.read(1)


    if root in '1234567890':
        return root
    else:
        return(root, tree(), tree())



# * 8 + 4 3

tupple1 = tree()
tupple2 = ['+', '4', '3']
tupple3 =['*', '8', ['+', '4', '3']]
tupple4 = ['*', ['-', '2', '8'], ['+', '4', '3']]

print(calculator(tupple1))
#print(calculator(tupple2))
#print(calculator(tupple3))
#print(calculator(tupple4))

#print(tree())