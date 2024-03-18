#!/usr/bin/python3
import sys

def pottery_prices(prices, current_item, length, value):
    if current_item==-1:
        return value
    else:
        s1 = pottery_prices(prices, current_item-1, length, value)

        s2 = 0
        s3 = 0
        if length >= current_item:
            s2 = pottery_prices(prices, current_item-1, length-(current_item+1), value + prices[current_item])
            s3 = pottery_prices(prices, current_item, length-(current_item+1), value + prices[current_item])
        
        return max(s1, s2, s3)


length=int(sys.stdin.readline().strip("\n"))
prices=[]
pr_list=sys.stdin.readlines()
for pr in pr_list:
    pr=pr.strip("\n").split()
    for x in pr:
        prices.append(float(x))

print('{:.2f}'.format(pottery_prices(prices, length-1, length-1, 0.0)))
