import sys

def matrix(M, input):
    
    if input[0] == 'row':
        row = ' '.join(map(str, M[int(input[1])-1]))
        result = f'{input[0]} {int(input[1])}: {row}'
        return result

    if input[0] == 'column':
        column = []
        
        for i in range(len(M)):
            column.append(M[i][int(input[1])-1])
        final = ' '.join(map(str, column))
        result = f'{input[0]} {input[1]}: {final}'
        return result
    
    if input[0] == 'element':
        result = f'{input[0]} {input[1]} {input[2]}: {M[int(input[1])-1][int(input[2])-1]}'
        return result






length = list(map(int, sys.stdin.readline().strip().split()))

M = []

for i in range(length[0]):
    row = list(map(int, sys.stdin.readline().strip().split()))
    linia = []
    for j in range(length[1]):
        linia.append(row[j])
    M.append(linia)

#print(M)

for line in sys.stdin:
    input = line.strip().split()
    if input != []:
        resultado = matrix(M, input)
        print(resultado)
        #print(len(M))


