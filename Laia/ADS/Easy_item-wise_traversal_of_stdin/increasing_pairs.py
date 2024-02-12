import sys

def increasing_pairs(seq):
    count = 0
    prev = seq[0]
    for number in seq:
        if number > prev:
            count += 1
        prev = number
    return count

n = int(sys.stdin.readline().strip())
for _ in range(n):
    linia = list(map(int, sys.stdin.readline().strip().split()))
    print(increasing_pairs(linia))
