import random

def get_random_number_g():
    for _ in range(10):
        numero_aleatori = random.randint(1, 100)
        yield numero_aleatori

res = get_random_number_g()
for x in res:
    print(x)


