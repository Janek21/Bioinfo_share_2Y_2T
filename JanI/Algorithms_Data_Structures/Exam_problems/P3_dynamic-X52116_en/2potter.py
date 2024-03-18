#!/usr/bin/python3
import sys

def pottery_prices(prices, max_l):
    M = [[ 0 for _ in range(len(prices)+1) ] for _ in range(max_l+1) ] 
    
    for bar_size in range(1, max_l+1):
        for piece in range(1, len(prices)+1):

            if piece<=bar_size: 
                
                if prices[piece-1]+ M[bar_size-piece][piece]>M[bar_size][piece-1]:
                    M[bar_size][piece]=prices[piece-1]+ M[bar_size-piece][piece]
                
                else:
                    M[bar_size][piece]=M[bar_size][piece-1]
            else:
                M[bar_size][piece]=M[bar_size][piece-1]

    
    return M[-1][-1]


def main():
    rod=sys.stdin.readline()
    text=sys.stdin.readlines()
    prices=[]
    for line in text:

        line=line.strip("\n").split()
        line=[float(x) for x in line]
        prices=prices+line

    return '{:.2f}'.format(pottery_prices(prices, int(rod)))

print(main())