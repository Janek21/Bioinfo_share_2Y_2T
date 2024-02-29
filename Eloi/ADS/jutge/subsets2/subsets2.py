from pytokr import pytokr

inp = pytokr()

rep = int(inp())

sets = []

def subset(l, pos, cand):
	if len(cand) == rep :
		sets.append(cand)
		return 
	if pos == -1:
		return 
	subset(l,pos-1,cand + [l[pos]])
	subset(l,pos-1,cand)
	
prev = []

for x in range(int(inp())):
	prev.append(inp())

subset(prev,len(prev)-1, [])


for y in sets[::-1]:
    st = ','.join(y)
    clau = '{}'
    print(f'{clau[0]}{st}{clau[1]}')

