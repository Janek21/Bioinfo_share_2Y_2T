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
    DP matrix D, init 0; D[w][j]:
      best value under weight limit w using only the first j objects
    Secondary matrix used to trace back the solution:
      best[w][j]: boolean value "take object j for solution with weight w?"
    '''
    D = [[ 0 for _ in range(n) ] for _ in range(max_w + 1) ]
    best = [ [ False for _ in range(n) ] for _ in range(max_w + 1) ] 
    
    '''
    initialization of the matrix
    values 0, bc so far we haven't considered any object
    '''
    
    for j in range(n):
        "init for zero weight: best and only option empty knapsack"
        D[0][j] = 0 # unnecesary bc we have already initialized the matrix with 0.
    for j in range(n): # traverse all the rows
        for w in range(1, max_w + 1): # traverse all the columns
            "update matrices at that cell"
            if D[w - weights[j]][j-1] + values[j] > D[w][j-1] and weights[j] <= w:
            # D[w - weights[j]][j-1] --> checks an entry of the matrix that can be far away.
            # weights[j] <= w <-- is possible object j??
            	# apply the recurrence we have before 
                "best is to take object j in"
                D[w][j] = D[w - weights[j]][j-1] + values[j] # take the M for 1 object
                best[w][j] = True # assign that the object is used
            else:
                "best is not to take it"
                D[w][j] = D[w][j-1]

    sol = list() # trace the solution
    w, i = max_w, n - 1
    while w > 0 and i >= 0:
        if best[w][i]: # if in that position there is a true
            sol.append(i) # take the object
            w -= weights[i] # reduce the weigth by the quantity that we have taken
        i -= 1 # reduce 1 column
    return sol, D[max_w][n-1] # take second value (and comma) out for testmod and Jutge

# ~ from doctest import testmod; testmod()


















