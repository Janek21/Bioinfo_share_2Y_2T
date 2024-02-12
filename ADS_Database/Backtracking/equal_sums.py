from pytokr import pytokr

inp = pytokr()

def simple_sum(a, lst, current_item, cand, solutions):
    if current_item == -1:
        if sum(cand) == a:
            solutions.append(cand)  
        return

    simple_sum(a, lst, current_item - 1, cand + [lst[current_item]], solutions)
    
    simple_sum(a, lst, current_item - 1, cand, solutions)

solutions = []
a = int(inp())
list = []
n_of_items = int(inp())
for _ in range(n_of_items):
    list.append(int(inp()))

simple_sum(a, list, len(list)-1, [], solutions)
for x in solutions:
    sol = "{" + ", ".join(map(str, x)) + "}"
    print(sol)
