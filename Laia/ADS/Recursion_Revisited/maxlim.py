def maxlim(m, k):
    '''
    >>> maxlim(1234, 1)
    4
    >>> maxlim(3234, 2)
    34
    >>> maxlim(32749, 2)
    79
    >>> maxlim(1917, 2)
    97
    >>> maxlim(32749, 18)
    32749
    >>> maxlim(2668037, 5)
    68037
    '''

    n = 0
    sols = maxlim_aux(str(m), k, n, '')
    return sols


def maxlim_aux(m, k, n, cands):
    if n == len(m) or len(cands) == k :
        if cands:
            return int(cands)
        return 0

    else:
        sol1 = maxlim_aux(m, k, n+1, cands)
        sol2 = maxlim_aux(m, k, n+1, cands+m[n])

    return max(sol1, sol2)


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)