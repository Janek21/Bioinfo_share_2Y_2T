#!/usr/bin/python3

def knapsacks_util(weights, values, current_item, max_w, cand, cand_w):
    if current_item==-1:
        if cand_w<=max_w:
            return[cand]
        else: 
            return list()
    else:
        sol=knapsacks_util(weights, values, current_item-1, max_w, cand, cand_w)
        res=knapsacks_util(weights, values, current_item-1, max_w, 
                            cand+[current_item], 
                            cand_w+weights[current_item])

        return sol+res


def knapsack(weights, values, n, max_w):

    sol = knapsacks_util(weights, values, n-1, max_w, [], 0) #all lists that are under max weight in a list
    t_max = 0
    for ls in sol: #filter through list of lists, get one that has max value
        total=0
        for x in ls:
            total+=values[x]
            
        if total>t_max:
            t_max=total
            mx=ls
    return mx

#weights =  [1, 1, 1, 1]
#values =  [3, 5, 7, 7]

#print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))

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
''' 
if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
'''