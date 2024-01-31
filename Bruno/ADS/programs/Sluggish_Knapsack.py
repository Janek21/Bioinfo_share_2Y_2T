
def knapsack(weights, values, n, limw):
    lista = []
    answer = []
    suma = 0
    z = finding_sum(weights, 0, 0, lista, answer, limw, suma)
    indexes = create_set_of_answers(z)
    result = maxima_suma(indexes, values)
    return result

def finding_sum(weights, start, i, lista, answer, limw, suma):
    if start == len(weights):
        return answer
    else:
        if i < len(weights):

            if suma + weights[i] <= limw:
                lista.append(i)
                suma += weights[i]
                i += 1
                return finding_sum(weights, start, i, lista, answer, limw, suma)
            else:
                i += 1
                return finding_sum(weights, start, i, lista, answer, limw, suma)
        else:
            answer.append(lista)
            suma = 0
            lista = []
            start += 1
            i = start
            return finding_sum(weights, start, i, lista, answer, limw, suma)

def create_set_of_answers(z):
    matrix = []
    for x in z:
        if x not in matrix:
            matrix.append(x)
    return matrix

def maxima_suma(indexes, values):
    max_value = 0
    for i in indexes:
        current_value = 0
        for j in i:
            current_value += values[j]
        if current_value > max_value:
            max_value = current_value
    return max_value



#weights = [1, 1, 1, 1]
#values = [3, 5, 7, 7]
#n = 4
#limw = 2
#bruno = knapsack(weights, values, n, limw)
#print(bruno)