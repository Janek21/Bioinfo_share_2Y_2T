import sys

def A_B(s):
    
    prev = ''
    a = 0
    length = 0
    winner = 0
    for x in s:
        if prev == '':
            prev = x
            if len(x)%2 != 0:
                length = len(x)
            else:
                return winner
                
        
        elif len(x)%2 == 0:
            return winner
        
        else:
            position = len(x)//2
            position2 = len(prev)//2
            if x[position] != prev[position2]:
                return winner
            prev = x
        
        winner += 1
    return '='
        
    
    




#def integregar(x):
    #return int(x)

#llista_int = map(integregar, s)
#print(llista_int)



n = sys.stdin.readline().strip()

s = sys.stdin.readline().split()

result = A_B(s)

if result == '=':
    print('=')
elif result%2 == 0:
    print('B')
elif result%2 != 0:
    print('A')
