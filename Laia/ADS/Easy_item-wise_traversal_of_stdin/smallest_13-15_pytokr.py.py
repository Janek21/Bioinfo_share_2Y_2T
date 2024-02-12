from pytokr import pytokr
item, items = pytokr(iter = True)

def smallest(lst):
    a = []
    for number in lst:
        if number % 13 == 0 and '5' in str(number):
            a.append(number)
    
    if len(a) == 0:
        return 'no one'
    return sorted(a)[0]

l = []
for num in items():
    num = int(num)
    while num != 0:
        l.append(int(num))
        num = int(item())
    print(smallest(l))
    l = []