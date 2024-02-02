from pytokr import pytokr
def trace(best, goal):
    coins = []
    while goal:
        use = best[goal]
        coins.append(use)
        goal -= use
    return coins

def minchange(goal, denoms):
    dptable = [float('inf')] * (goal + 1)
    best = [0] * (goal + 1)

    dptable[0] = 0

    for quant in range(1, goal + 1):
        for coin in denoms:
            if coin <= quant and 1 + dptable[quant - coin] < dptable[quant]:
                dptable[quant] = 1 + dptable[quant - coin]
                best[quant] = coin

    if dptable[goal] > goal:
        return "no"
    else:
        return len(trace(best, goal))

item = pytokr()

while True:
    denoms = list()
    goal = int(item())
    num = int(item())
    for x in range(num):
        denoms.append(int(item()))
    sol = minchange(goal, denoms)
    print(sol)

