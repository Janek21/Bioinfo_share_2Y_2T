from pytokr import pytokr

def canvi_minim(amount, n, denominations):
    # Sort denominations in descending order
    denominations.sort(reverse=True)
    coins_used = []

    # Iterate through the sorted denominations
    for coin in denominations:
        # Subtract the coin from the amount as many times as possible
        while amount >= coin:
            coins_used.append(coin)
            amount -= coin

    # If the amount is not zero, it means the change cannot be made with the given denominations
    if amount > 0:
        return "no"
    else:
        # Return True if the number of coins used equals n, otherwise False
        return len(coins_used) == n

item = pytokr()
while True:
    s = list()
    n = int(item())
    for x in range(n):
        s.append(int(item()))
    c = sum(s)
    euro = [1,2,5,10,20,50,100,200]
    sol = canvi_minim(c, n, euro)
    if sol == True:
        print('si')
    else:
        print('no')
