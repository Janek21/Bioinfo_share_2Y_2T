from pytokr import pytokr
item = pytokr()

def subset(l, pos, cand):
	if pos >= len(l):
		sets.append(cand)
		return 
	subset(l, pos+1, cand + [l[pos]])
	subset(l, pos+1, cand)


item = pytokr()
n = int(item())
n_words = int(item())
words = []

sets = []

for _ in range(n_words):
    words.append(item())

subset(words, 0, [])

lista = []
for x in sets:
    if len(x) == n:
        lista.append(x)
#print(lista)

#[::-1]
for y in lista:
    st = ','.join(y)
    clau = '{}'
    print(f'{clau[0]}{st}{clau[1]}')