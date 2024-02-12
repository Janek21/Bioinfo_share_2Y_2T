## NOMES RETORNA 1 SOLUCIÓ

def knapsack(weights, values, n, capacity):
    '''
    >>> weights =  [7, 8, 3]
    >>> values =  [3000, 4000, 2000]
    >>> print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))
    5000
    >>> weights =  [7, 8, 3]
    >>> values =  [3000, 6000, 2000]
    >>> print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))
    6000
    >>> weights =  [1, 1, 1, 1]
    >>> values =  [3, 5, 7, 7]
    >>> print(sum(values[obj] for obj in knapsack(weights, values, 4, 2)))
    14
    '''

    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)] # incialitzar matriu

    for i in range(1, n + 1): # per cada row (elements)
        for w in range(1, capacity + 1): # per cada col (capacitats)
            if weights[i - 1] <= w: # element actual te un weight <= el maxim per la cel·la on et trobes
                agafar = values[i - 1] + dp[i - 1][w - weights[i - 1]] # item + 1 row abans i x cols abans
                no_agafar = dp[i - 1][w] # mateix item que adalt
                dp[i][w] = max(no_agafar, agafar) # mirar que es més gran
            else: # element actual te un weight massa gran
                dp[i][w] = dp[i - 1][w] # agafar el valor d'adalt

    # reconstruir la solució
    result = []  # index dels elements
    w = capacity 
    v = dp[n][capacity] # valor maxim obtingut

    for i in range(n, 0, -1): # iterar sobre les rows (reverse)
        if v != dp[i - 1][w]: # valor canvia respecte la row anterior (no s'inclou l'actual)
            result.append(i - 1) # agefir index element actual
            v -= values[i - 1] # restar valor actual al valor total
            w -= weights[i - 1] # restar pes actual al pes total

    return result

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)