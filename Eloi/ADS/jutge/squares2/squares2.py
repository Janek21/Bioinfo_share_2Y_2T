import sys

def square(x):
	return [str(num%10) if (num+1)%int(x)!=0 else f'{num%10}\n' for num in range(int(x)**2)]
	
final = map(square, sys.stdin.readlines())
for case in final:print(''.join(case))
