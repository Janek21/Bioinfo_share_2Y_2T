
from pytokr import pytokr

def trace(best, goal):
    coins = []
    while goal:
        use = best[goal]
        coins.append(use)
        goal -= use
    return coins

def minchange(goal, denoms):
    denoms = [0] + list(denoms) # placeholder
    dptable = {}
    best = {}
    for quantity in range(goal + 1):
        "init table for no coins"
        dptable[0, quantity] = float("inf")
    for coin in range(len(denoms)):
        dptable[coin, 0] = 0
    for quantity in range(1, goal + 1):
        '''
        dptable[coin, quantity]: 
        how many coins up to that one needed to add up to quantity
        '''
        for coin in range(1, len(denoms)):
            "try using it"
            if (denoms[coin] <= quantity and 
                1 + dptable[coin, quantity - denoms[coin]] < dptable[coin - 1, quantity]):
                dptable[coin, quantity] = 1 + dptable[coin, quantity - denoms[coin]]
                best[quantity] = denoms[coin]
            else:
                dptable[coin, quantity] = dptable[coin - 1, quantity]
    if dptable[len(denoms) - 1, goal] <= goal:
        print(trace(best, goal))
    return -1 if dptable[len(denoms) - 1, goal] > goal else dptable[len(denoms) - 1, goal]

item, items = pytokr(iter = True)

for case in items():
    goal = int(case)
    denoms = []
    for _ in range(int(item())):
        "statement guarantees at least one"
        denoms.append(int(item()))
    r = minchange(goal, denoms)
    if r == -1:
        print("no")
    else:
        print(r)


