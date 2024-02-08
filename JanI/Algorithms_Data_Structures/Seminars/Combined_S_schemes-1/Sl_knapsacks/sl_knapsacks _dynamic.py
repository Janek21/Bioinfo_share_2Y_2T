#!/usr/bin/python3


def max_value(best, weights, values, max_w):
    items_index = []
    for i in range(len(best)+1):
        for j in range(i+1, len(best)+1):

            w_comb=best[i:j]

            if sum(w_comb)<=max_w:
                items_index.append(w_comb)

    m_value=0
    for ls in items_index:

        if -1 not in ls: #check lists that don't contain -1
            correspondent_value=0

            for w in ls: #for each weight sublist (combination <=10) sum up all of its corresponding values
                correspondent_value+=values[weights.index(w)]

            if correspondent_value>m_value: #if the total value of the sublist is the greatest so far, it becomes max value
                m_value=correspondent_value

    return m_value


def knapsack(weights, values, n, max_w):
    denoms=[0]+weights
    table=[float("inf")]*(max_w+1) #len table is n+1 at max, n is max len, +1 is for 0 on denoms
    table[0]=0 #first position =0 like in denoms
    best=[-1]*(max_w+1)

    for w in range(1,len(denoms)): #for weights in original weight list (for w in denoms can't be done because 0 would be included)
        #perhaps for w in weights? int(w)
        for pos in range(denoms[w], max_w+1):
            #from the weight (in weights list) you are "looking at" "sum?" up to max_w (in values, adds up values until they == max value)

            if 1+table[pos-denoms[w]]<table[pos]:
                table[pos]=1+table[pos-denoms[w]]
                best[pos]=denoms[w]

    print(best)
    return max_value(best, weights, values, max_w)
    #return best


weights =  [1, 1, 1, 1]
values =  [3, 5, 7, 7]
print(knapsack(weights, values, 4, 2))
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
'''
'''
if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
'''

'''
while max_w: #weight does not need to fit perfectly, <10 and not ==10, then take highest value
    use = best[max_w]
    print(max_w)
    correspondent_value=values[weights.index(use)]
    items_index.append(correspondent_value)
    max_w -= use

w_list=[]
for i in range(len(best)):
    current_w=best[i]
    for j in range(i+1, len(best)):
        w=best[j]
        if w!=-1:
            current_w+=w
            if current_w<=max_w:
                w_list.append(w)
            if current_w>max_w and w_list:
                items_index.append(w_list)
                w_list=[]
'''