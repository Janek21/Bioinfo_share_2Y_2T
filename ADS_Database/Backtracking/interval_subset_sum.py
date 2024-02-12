def sub_sum_interval(L, U, t):
    '''
    >>> sol = sub_sum_interval(96, 104, [60, 15, 25, 95, 80, 5, 10, 5, 10, 75])
    >>> print('Sum in interval [ 96 ,  104 ): ', 96  <= sum(sol) <  104 )
    Sum in interval [ 96 ,  104 ):  True
    >>> print(len(sol))
    2
    >>> sol = sub_sum_interval(10, 20, [55, 55])
    >>> print('Sum in interval [ 10 ,  20 ): ', 10  <= sum(sol) <  20 )
    Sum in interval [ 10 ,  20 ):  False
    >>> print(len(sol))
    0
    >>> sol = sub_sum_interval(40, 40, [25, 15])
    >>> print('Sum in interval [ 40 ,  40 ): ', 40  <= sum(sol) <  40 )
    Sum in interval [ 40 ,  40 ):  False
    >>> print(len(sol))
    0
    >>> sol = sub_sum_interval(30, 40, [5, 5, 5, 5, 5, 10])
    >>> print('Sum in interval [ 30 ,  40 ): ', 30  <= sum(sol) <  40 )
    Sum in interval [ 30 ,  40 ):  True
    >>> print(len(sol))
    5
    >>> sol = sub_sum_interval(30, 40, [20, 20])
    >>> print('Sum in interval [ 30 ,  40 ): ', 30  <= sum(sol) <  40 )
    Sum in interval [ 30 ,  40 ):  False
    >>> print(len(sol))
    0
    '''
    def find_subset_sum(sum, ind, subset):
        if L <= sum < U: 
            sol.append(subset)
        if ind == len(t):   
            return
        else:
            find_subset_sum(sum + t[ind], ind + 1, subset + [t[ind]])   
            find_subset_sum(sum, ind + 1, subset)
    sol = []
    find_subset_sum(0, 0, [])
    if sol:
        return min(sol, key=len)
    else:
        return []


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

