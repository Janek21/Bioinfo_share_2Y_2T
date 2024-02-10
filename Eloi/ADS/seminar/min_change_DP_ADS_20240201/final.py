from pytokr import pytokr

def coin_trace(best, goal):
    """Trace the coins used to make up the goal."""
    coins = []
    while goal:
        use = best[goal]
        coins.append(use)
        goal -= use
    return coins

def min_change_count(goal, denominations):
    """Calculate the minimum number of coins needed to make up the goal."""
    dp_table = [float('inf')] * (goal + 1)
    best_coin = [0] * (goal + 1)

    dp_table[0] = 0

    for quantity in range(1, goal + 1):
        for coin in denominations:
            if coin <= quantity and 1 + dp_table[quantity - coin] < dp_table[quantity]:
                # Update the dynamic programming table if a better solution is found.
                dp_table[quantity] = 1 + dp_table[quantity - coin]
                best_coin[quantity] = coin

    if dp_table[goal] > goal:
        return "no"  # If it's not possible to make up the goal, return "no".
    else:
        return len(coin_trace(best_coin, goal))  # Return the minimum number of coins.

item, items = pytokr(iter=True)

for case in items():
    goal = int(case)
    denominations = []
    for _ in range(int(item())):
        # "statement guarantees at least one"
        denominations.append(int(item()))

    # Print the result for each case.
    print(min_change_count(goal, denominations))
