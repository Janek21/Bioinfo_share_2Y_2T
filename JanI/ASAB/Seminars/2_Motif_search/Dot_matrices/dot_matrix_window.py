#!/usr/bin/python3
#no pot ser que amb window size 2 F i A que estan a files seguides tinguin dots (si es per columnes tampoc pot ser, ja que F i A estan a la 0 i 5) 
def dot_matrix_window(seq1, seq2, size):
    M=[[" " for _ in range(len(seq1))] for _ in range(len(seq2))]
    for i in range(0, len(seq1)):
        print(i)
        for j in range(0, len(seq2), size):
            #print(j)
            if seq1[i]==seq2[j]:
                M[j][i]="o"

    return M

print(dot_matrix_window("FASTCAT", "FATRAT", 2))
