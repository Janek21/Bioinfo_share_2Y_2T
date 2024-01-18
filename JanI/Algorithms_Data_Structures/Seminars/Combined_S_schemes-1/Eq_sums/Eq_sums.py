#!/usr/bin/python3
import sys

def eq_sum(numbers, value, i):
    if i<=-1:
        return 
    x=numbers[i]
    for y in numbers:
        ?


value=int(sys.stdin.readline().strip())
no=sys.stdin.readline().strip()
numbers=sys.stdin.readline().strip().split()

print(eq_sum(numbers, value, len(numbers)))