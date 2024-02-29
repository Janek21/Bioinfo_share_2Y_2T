import sys

def compute_freq(p, index, D1):
    if index >= len(p):
        return D1
    else:
        if p[index] not in D1:
            D1[p[index]] = 1
        else:
            D1[p[index]] += 1
        index += 1
        return compute_freq(p, index, D1)
    
def comparing_freq(D1, D2):
    for x in D1.keys():
        if x not in D2.keys():
            return False
        if D1[x] > D2[x]:
            return False
    return True

def compare_digits(p, q):
    '''
    >>> compare_digits(123, 321)
    True
    >>> compare_digits(1213, 33221)
    False
    >>> compare_digits(12, 22)
    False
    >>> compare_digits(314159, 112233456789)
    True
    '''
    p = str(p)
    q = str(q)
    D1 = {}
    D2 = {}
    index = 0
    D_1 = compute_freq(p, index, D1)
    index = 0
    D_2 = compute_freq(q, index, D2)
    return comparing_freq(D_1, D_2)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)