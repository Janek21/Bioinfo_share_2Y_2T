import sys

def even_vowels(lst):
    count = 0
    for line in lst:
        for word in line:
            c = 0
            for x in word:
                if x in "aeiou":
                    c += 1
            if c % 2 == 0:
                count += 1
    return count
            
lst = []
for line in sys.stdin:
    lst.append(line.strip().split())
print(even_vowels(lst))