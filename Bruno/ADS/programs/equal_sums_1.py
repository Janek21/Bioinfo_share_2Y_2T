import sys


def sumsset(numbers, s, index, starter, current, final):

    if index == len(numbers)-1:
        if s - numbers[index] == 0:
            current.append(numbers[index])
            final.add(current)
            starter += 1
            current = []
            index = 0
            return sumsset(numbers, s, index, starter, current, final)
    
    elif starter == len(numbers)-1:
        return final
    
    else:
        if s - numbers[index] > 0:
            current.append(numbers[index])
            index += 1
            return sumsset(numbers, s, index, starter, current, final)

def creator(numbers, s):
    index = 0
    starter = 0
    current = []
    final = set()
    return sumsset(numbers, s, index, starter, current, final)

def main():

    s = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    numbers = sys.stdin.readline().split()
    numbers = [int(x) for x in numbers]
    
    print(creator(numbers, s))

if __name__ == '__main__':
    main()
