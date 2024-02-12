from pytokr import pytokr

def minimum_change(euros, cents):
    # Define the denominations for euros and cents
    euro_denominations = [1,   2,   5,   10,   20,   50,   100,   200,   500]
    cent_denominations = [1,   2,   5,   10,   20,   50]

    # Initialize the DP table for euros and cents separately
    dp_euros = [float('inf')] * (euros +   1)
    dp_cents = [float('inf')] * (cents +   1)
    
    # Initialize the trace tables for euros and cents
    trace_euros = [[] for _ in range(euros +  1)]
    trace_cents = [[] for _ in range(cents +  1)]

    # Base case:   0 euros and   0 cents require   0 notes/coins
    dp_euros[0] = dp_cents[0] =   0

    # Calculate the minimum number of notes/coins for each denomination
    for i in range(1, euros +   1):
        for coin in euro_denominations:
            if coin <= i:
                if dp_euros[i - coin] +   1 < dp_euros[i]:
                    dp_euros[i] = dp_euros[i - coin] +   1
                    trace_euros[i] = trace_euros[i - coin] + [coin]

    for i in range(1, cents +   1):
        for coin in cent_denominations:
            if coin <= i:
                if dp_cents[i - coin] +   1 < dp_cents[i]:
                    dp_cents[i] = dp_cents[i - coin] +   1
                    trace_cents[i] = trace_cents[i - coin] + [coin]

    euro_combination = trace_euros[euros]
    cent_combination = trace_cents[cents]
    min_eur = {500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
    for key in euro_combination:
        min_eur[key] += 1
    min_cent = {50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
    for key in cent_combination:
        min_cent[key] += 1
    return min_eur, min_cent

item = pytokr()

eur = int(item())
cent = int(item())
min_eur, min_cent = minimum_change(eur, cent)

print(f'Banknotes of 500 euros: {min_eur[500]}')
print(f'Banknotes of 200 euros: {min_eur[200]}')
print(f'Banknotes of 100 euros: {min_eur[100]}')
print(f'Banknotes of 50 euros: {min_eur[50]}')
print(f'Banknotes of 20 euros: {min_eur[20]}')
print(f'Banknotes of 10 euros: {min_eur[10]}')
print(f'Banknotes of 5 euros: {min_eur[5]}')
print(f'Coins of 2 euros: {min_eur[2]}')
print(f'Coins of 1 euro: {min_eur[1]}')
print(f'Coins of 50 cents: {min_cent[50]}')
print(f'Coins of 20 cents: {min_cent[20]}')
print(f'Coins of 10 cents: {min_cent[10]}')
print(f'Coins of 5 cents: {min_cent[5]}')
print(f'Coins of 2 cents: {min_cent[2]}')
print(f'Coins of 1 cent: {min_cent[1]}')

