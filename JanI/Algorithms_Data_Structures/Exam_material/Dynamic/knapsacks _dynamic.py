#!/usr/bin/python3


def knapsack(weights, values, n, max_w):
	#DP matrix D, init 0; D[w][j]: <- has values, bottom right is best value -> to see ites that corrspond to value we use a traceback matrix
	#best value under weight limit (w) using only first j objects
	#Secondary matric used to trace back solution
	#best[w][j]: boolean value  for "take object j for solutions with weight w?"
    D=[[0 for _ in range(n)] for _ in range(max_w+1)]
    best=[[False for _ in range(n)] for _ in range(max_w+1)]

    for j in range(n):
        #"define column" for zero weight, it will have value 0 
        D[0][j]=0
    for j in range(n):
          for w in range(1, max_w+1):
                #update the matrix at concrete cell
                #value of last entry (last weight=current w- weight of current (row? what is j) last value is in j-1)+value of current (values [j])
                if D[w - weights[j]][j-1] + values[j] > D[w][j-1] and weights[j] <= w:  #if ? is bigger than the previous one and its weight is smaller or equal than the maximum weight
                    #if ^^ is true take object j in (new weight(w-weights[j]) and value)
                    D[w][j]=D[w-weights[j]][j-1] + values[j]
                    best[w][j] = True
                else:
                    #if the if statement no es compleix define current the same as last (same weight and value )
                    D[w][j]=D[w][j-1]
    sol=[] #backtrace the solution
    w, i = max_w, n - 1
    #max_w+1= length of a row (number of columns)in the table (we need to have from 0 to the number)
    #n= 3= number of rows in the table also = to weight used for the row, first, second, etc(0, 1, ...) in weights list
    while w>0 and i>=0:
        #bottom right is best value, so we start from last position of last list, we go up-left from there
        if best[w][i]: #if this position == True -> takes object j as solution under max_w
            sol.append(i) #append row number (equals to position in weights list)
            w =w-weights[i] #retrocede the same number of columns as the weight that corresponds to the position you appended
        i=i-1 #retrocede 1 row (n=3 -> i=2 in first iteration i=2 -> i=1)
    #return sol, D[max_w][n-1] #return first positions that are True from bottom right and also the bottom-right value
    return sol


weights =  [7, 8, 3]
values =  [3000, 4000, 2000]
#print(knapsack(weights, values, 3, 10))
#max_w=10
#print(knapsack(weights, values, 3, max_w))
#best=knapsack(weights, values, 3, max_w)

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


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
'''
