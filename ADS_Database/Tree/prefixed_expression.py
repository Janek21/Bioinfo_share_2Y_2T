from pytokr import pytokr

item = pytokr()


def prefixed_expression(tokens):
    if len(tokens) == 1:
        return int(tokens[0])
    else:
        if tokens[0] == '+':
            result = prefixed_expression(tokens[1]) + prefixed_expression(tokens[2])
        elif tokens[0] == '-':
            result = prefixed_expression(tokens[1]) - prefixed_expression(tokens[2])
        elif tokens[0] == '*':
            result = prefixed_expression(tokens[1]) * prefixed_expression(tokens[2])
        return result


def tree():
    root = item()

    if root == ' ':
        root = item()


    if root in '1234567890':
        return root
    else:
        return(root, tree(), tree())

token_list = tree()
print(token_list)
sol = prefixed_expression(token_list)
print(sol)

