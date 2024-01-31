from pytokr import pytokr

inp = pytokr()

def min_monedes(c, n, valors):
    def backtrack(index, current_sum, coins_used):
        nonlocal min_coins

        if current_sum == c:
            min_coins = min(min_coins, coins_used)
            return

        if current_sum > c or coins_used >= min_coins or index >= len(valors):
            return

        x = valors[index]
        backtrack(index, current_sum + x, coins_used + 1)
        backtrack(index + 1, current_sum, coins_used)

    min_coins = float('inf')
    backtrack(0, 0, 0)

    if min_coins != float('inf'):
        return min_coins 
        
    else:
        return "no"

while True:   
    c = int(inp())
    n = int(inp())
    valors = []
    for _ in range(n):
        valors.append(int(inp()))

    sol = min_monedes(c, n, valors)
    print(sol)

