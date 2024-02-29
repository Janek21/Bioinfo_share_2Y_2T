import sys 


def count_vowels(s):
    counterword = 0
    for x in s:
        countervowel = 0
        for y in x:
            
            if y in 'aeiou':
                countervowel += 1
        
        if countervowel%2 == 0:
            counterword += 1
    
    return counterword



    
s = sys.stdin.readlines()
z = [word for line in s for word in line.strip().split()]

resultado = count_vowels(z)

print(resultado)
