def sub_sum_interval(lower, upper, num):
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
    n = len(num)-1
    res = s(upper, lower, num, n, [], 0)
    if res:
        return min(res, key = len)
    return []

def s(U, L, num, current_item, cand, suma):
    if current_item == -1:
        if L <= suma < U:
            return [cand]
        return []
    else:
        sol1 = s(U, L, num, current_item-1, cand, suma)
        sol2 = s(U, L, num, current_item-1, cand + [num[current_item]], suma + num[current_item])
        return sol1 + sol2

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
    
