import sys

a = sys.stdin.readline().strip()

lista = []
lista =  list(map(float, sys.stdin.readline().strip().split()))



constant = 1
i = len(lista) - 1
resultado = 0
a = float(a)

while 0 <= i:
    resultado += float(lista[i]) * float(constant)
    i -= 1
    constant = constant * a

print("{0:.4f}".format(resultado))