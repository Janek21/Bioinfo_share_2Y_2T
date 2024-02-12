from many_finds import many_finds


def indexing(string):
    '''
    >>> indexing("THEFASTCAT")
    [('A', [4, 8]), ('AS', [4]), ('AST', [4]), ('ASTC', [4]), ('ASTCA', [4]), ('ASTCAT', [4]), ('AT', [8]), ('C', [7]), ('CA', [7]), ('CAT', [7]), ('E', [2]), ('EF', [2]), ('EFA', [2]), ('EFAS', [2]), ('EFAST', [2]), ('EFASTC', [2]), ('EFASTCA', [2]), ('EFASTCAT', [2]), ('F', [3]), ('FA', [3]), ('FAS', [3]), ('FAST', [3]), ('FASTC', [3]), ('FASTCA', [3]), ('FASTCAT', [3]), ('H', [1]), ('HE', [1]), ('HEF', [1]), ('HEFA', [1]), ('HEFAS', [1]), ('HEFAST', [1]), ('HEFASTC', [1]), ('HEFASTCA', [1]), ('HEFASTCAT', [1]), ('S', [5]), ('ST', [5]), ('STC', [5]), ('STCA', [5]), ('STCAT', [5]), ('T', [0, 6, 9]), ('TC', [6]), ('TCA', [6]), ('TCAT', [6]), ('TH', [0]), ('THE', [0]), ('THEF', [0]), ('THEFA', [0]), ('THEFAS', [0]), ('THEFAST', [0]), ('THEFASTC', [0]), ('THEFASTCA', [0]), ('THEFASTCAT', [0])]
    '''

    out = set()
    n = len(string)
    for i in range(n):
        for j in range(i, n + 1):
            out.add(string[i:j])
    out.remove('')

    ls = []
    for sub in sorted(list(out)):
        ls.append((sub, many_finds(sub, string)))
    return ls


if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)