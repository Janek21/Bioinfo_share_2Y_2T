import random

def get_random_number_ng():
    result = []
    for _ in range(10):
        rand_int = random.randint(1, 100)
        result.append(rand_int)
    return result

res = get_random_number_ng()
print(res)


