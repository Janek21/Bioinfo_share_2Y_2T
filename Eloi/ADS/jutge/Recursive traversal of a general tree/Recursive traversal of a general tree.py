from pytokr import pytokr

item, items= pytokr(iter=True)

global_list = []
num = int(item())

for pack in range(num):
	key,value = item(),item()
	global_list.append((int(key),int(value)))
	
print(global_list)

def traversal(L,n):
	if L[n][1] == 0:
		  return 
	return traversal(L,n+1)
