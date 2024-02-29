from pytokr import pytokr

item = pytokr()

max = int(item())

n = int(item())

numbers = []

for _ in range(n):
    numbers.append(int(item()))

candidato = []

solucion = []

index = n - 1

def sumar(numbers, index, max, candidato, solucion):
    if index == -1:
        if sum(candidato) == max:
            solucion.append(candidato)
        return
    else:
        sumar(numbers, index - 1, max, candidato + [numbers[index]], solucion)
        sumar(numbers, index - 1, max, candidato, solucion)

sumar(numbers, index, max, candidato, solucion)

for x in solucion:
    clau = '{}'
    st = f'{x}'
    print(f'{clau[0]}{st[1:-1]}{clau[1]}')