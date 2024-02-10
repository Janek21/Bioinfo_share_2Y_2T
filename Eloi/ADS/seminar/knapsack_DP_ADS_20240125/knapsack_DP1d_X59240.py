"""
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
>>> weights =  [1]
>>> values =  [1]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 1, 2)))
1
>>> weights =  [2, 1, 1, 1, 1]
>>> values =  [1, 1, 1, 1, 1]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 6)))
5
>>> weights =  [3, 2, 1, 1, 1]
>>> values =  [1, 1, 1, 1, 1]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 6)))
4
>>> weights = [9, 8, 12, 11, 7]
>>> values = [16, 15, 24, 23, 13]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 26)))
51
"""

def knapsack(weights, values, n, max_w):
    '''
    DP implementing DP matrix with two rows: previous and current;
      at the beginning of loop i in range(n), prev[w] is the
      best value under weight limit w using only objects below i;
      thus init 0 as using only 0 objects, and prev[0] == 0 always
    Secondary matrix to trace back the solution.
    '''
    prev = [ 0 for _ in range(max_w + 1) ]
    best = [ [ False for _ in range(n) ] for _ in range(max_w + 1) ]
    curr = [ 0 for _ in range(max_w + 1) ] # just placeholders at this point
    
    for j in range(n):
        "find out what happens if object j can be used as well"
        for w in range(1, max_w + 1): 
            "update matrices at that cell"
            if weights[j] <= w and prev[w - weights[j]] + values[j] > prev[w]:
                "best is to take object j in"
                curr[w] = prev[w - weights[j]] + values[j]
                best[w][j] = True
            else:
                "best is not to take it"
                curr[w] = prev[w]
        prev, curr = curr, prev

    sol = list() # trace the solution
    w, i = max_w, n - 1
    while w > 0 and i >= 0:
        if best[w][i]:
            sol.append(i)
            w -= weights[i]
        i -= 1
    return sol, prev[max_w] # take second value (and comma) out for testmod and Jutge

# ~ from doctest import testmod; testmod()

