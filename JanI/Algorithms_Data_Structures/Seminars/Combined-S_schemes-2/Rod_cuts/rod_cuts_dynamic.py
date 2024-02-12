#!/usr/bin/python3

import sys

#n=first value


def rod_cut(values,  max_l): #maxl=len(values)
    M = [[ 0 for _ in range(len(values)+1) ] for _ in range(max_l+1) ] #per casualitat son iguals (no comptem columna extra de 0)
    
    for bar_size in range(1, max_l+1): #la meva barra sencera
        for piece in range(1, len(values)+1): #el meu tall

            if piece<=bar_size: #tall mes petit que el tros de barra que estic mirant
                #M[bar_size][piece]=max(values[piece-1]+ M[bar_size-piece][piece],M[bar_size-1][piece])
                
                if values[piece-1]+ M[bar_size-piece][piece]>M[bar_size][piece-1]:#price before+now (column above+ price on current index) is bigger than last (above)
                #if price of current+D[row above][column] > price of last
                    M[bar_size][piece]=values[piece-1]+ M[bar_size-piece][piece] #bar_size-piece -> 5-3 -> tinc una barra de 2
                
                else: #other else won't do, it will ignore it
                    M[bar_size][piece]=M[bar_size][piece-1]
            else:
                M[bar_size][piece]=M[bar_size][piece-1]

    
    return M[-1][-1]

    
#max_w=5
#table=[1.0, 2.4, 3.0, 4.0, 4.5]
#print((rod_cut(table, 0.0, max_w, [], 0, 0))) #add max

def main():
    rod=sys.stdin.readline()
    text=sys.stdin.readlines()
    values=[]
    for line in text:

        line=line.strip("\n").split()
        line=[float(x) for x in line]
        values=values+line

    return '{:.2f}'.format(rod_cut(values, int(rod)))

print(main())
