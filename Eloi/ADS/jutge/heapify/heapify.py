from pytokr import pytokr

lista = [3,5,2,8,4,6,1]

def siftup(i,L):
	if L[i] < L[(i - 1)//2]:
		L[i],L[(i - 1)//2] = L[(i - 1)//2],L[i]
		siftup((i - 1)//2, L)
	return L
print(siftup(len(lista)-1,lista))

