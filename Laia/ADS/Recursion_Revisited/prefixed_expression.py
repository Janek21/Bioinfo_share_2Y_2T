from pytokr import pytokr
read = pytokr()

def read_input():
    root = read()
    if root.isnumeric():
        return root
    return (root, read_input(), read_input())
    
def calculator(lst):
    if len(lst) == 1:
        return int(lst[0])
    else:
        op = lst[0]
        if op == '+':
            return calculator(lst[1]) + calculator(lst[2])
        elif op == '-':
            return calculator(lst[1]) - calculator(lst[2])
        else:
            return calculator(lst[1]) * calculator(lst[2])
        
inp = read_input()
print(calculator(inp))
