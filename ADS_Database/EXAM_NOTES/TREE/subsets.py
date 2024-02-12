from pytokr import pytokr

inp = pytokr()
def subsets(list, current_item, cand, solutions):
    if current_item == -1:
        solutions.append(cand)
        return 
    else:
        subsets(list, current_item-1, cand, solutions)
        subsets(list, current_item-1, cand + [list[current_item]], solutions)

solutions = []
cand = []
list =[]
num_of_items = inp()
for _ in range(int(num_of_items)):
    list.append(inp())
current_item = len(list)-1

subsets(list, current_item, cand, solutions)
for x in sorted(solutions):
    print('{' + ','.join(x)+'}')

