import sys

def sections(a, b, seq):
    begin = False
    lst = []
    for numb in seq:
        if numb == b and begin == True:
            return lst
        
        lst.append(str(numb))
        if numb == a and begin == False:
            lst = []
            begin = True

for line in sys.stdin:
    line = list(map(int, line.strip().split()))
    a = line[0]
    b = line[1]
    seq = list(map(int, sys.stdin.readline().strip().split()))
    res = sections(a, b, seq)
    if res == None or res == []:
        print()
    else:
        print(' '.join(res)+ ' ')
    print('----------')