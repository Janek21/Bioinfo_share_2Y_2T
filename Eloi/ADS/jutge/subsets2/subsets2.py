from pytokr import pytokr

inp = pytokr()

rep = int(inp())

sets = []

def subset(l, pos, cand):
	if pos == len(l):
		sets.append(cand)
		return 
	if len(cand) == rep-1:
		subset(l, pos+1, cand + [l[pos]])
	subset(l, pos+1, cand)

prev = []
for x in range(int(inp())):
	prev.append(inp())

subset(prev,0, [])


for y in sets[::-1]:
    st = ','.join(y)
    clau = '{}'
    print(f'{clau[0]}{st}{clau[1]}')