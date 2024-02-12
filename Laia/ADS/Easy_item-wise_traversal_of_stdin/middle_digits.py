import sys

def middle_digits(seq):
    c = 0

    index = len(seq[0])//2
    middle_dig = seq[0][index]

    for number in seq:
        if len(number) % 2 == 0:
            return c
        index = len(number)//2
        middle = number[index]

        if middle != middle_dig:
            return c
        
        c += 1

    return -1


n = int(sys.stdin.readline().strip())
seq = list(map(str, sys.stdin.readline().strip().split()))
res = middle_digits(seq)
if res == -1:
    print("=")
elif res % 2 == 0:
    print("B")
else:
    print("A")