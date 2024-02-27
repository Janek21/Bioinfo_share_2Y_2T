from pytokr import pytokr

sets = []
def subset(l, pos, cand):
	if pos >= len(l):
		sets.append(cand)
		return 
	subset(l, pos+1, cand + [l[pos]])
	subset(l, pos+1, cand)


def main():

    item = pytokr()
    n = int(item())
    words = []
    #sets = []
    
    for _ in range(n):
        words.append(item())
    

    subset(words, 0, [])


    for y in sets[::-1]:
        st = ','.join(y)
        clau = '{}'
        print(f'{clau[0]}{st}{clau[1]}')



if __name__ == '__main__':
    main()