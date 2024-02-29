import sys

def choose_num(s):
    smaller = 'no one'
    for x in s:
        if int(x)%13 == 0 and '5' in x:
            if smaller != 'no one':
                if x < smaller:
                    smaller = x
            else:
                smaller = x
    
    return smaller

for line in sys.stdin:
    s = line.strip().split()

    print(choose_num(s))