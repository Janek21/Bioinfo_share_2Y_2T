from pytokr import pytokr
item, items = pytokr(iter = True)

def even(lst):
    prev = ''
    for i in range(len(lst)):
        if i % 2 == 0:
            if lst[i] <= prev:
                return 'Even-Position Words Not Ascending.'
            prev = lst[i]
    return 'Even-Position Words Ascending.'
        
lst = []
for word in items():
    lst.append(word)
print(even(lst))