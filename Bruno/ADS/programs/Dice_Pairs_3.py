import sys

def number_counter(s):
    dict = {}
    for x in s:
        if int(x) not in dict.keys():
            dict[int(x)] = 1
        else:
            dict[int(x)] += 1
    #print(sorted(dict.items()))
    return sorted(dict.items())




x = 1
for line in sys.stdin:
    s = line.strip().split()

    if x == 1:
        result = number_counter(s)
        for x in result:
            print(f'{x[0]}: {x[1]}')
        x = 2

    else:
        print('-----')
        result = number_counter(s)
        for x in result:
            print(f'{x[0]}: {x[1]}')
    