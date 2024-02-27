from pytokr import pytokr

item = pytokr()

def readtree(countL, countR, L, R):
    root = int(item())
    if countL == L or countR == R:
        return tuple()
    else:
        countL += 1
        countR += 1
        return (root, readtree(countL, countR, L, R), readtree(countL, countR, L, R))
    
    total_size = int(item())
    