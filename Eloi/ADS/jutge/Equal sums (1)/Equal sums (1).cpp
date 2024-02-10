#include <string>
#include <vector>


using namespace std;

inp = pytokr()


void equal_sum(total, lista, current_item, cand, solutions){
    if (current_item == -1){
        if (sum(cand) == total){
            solutions.insert(cand)  
         }
        return
	}
    equal_sum(total, lista, current_item - 1, cand + [lista[current_item]], solutions)
    equal_sum(total, lista, current_item - 1, cand, solutions)
}

#Read input
total << cin
size << cin
lista = []
for _ in range(size):
    lista.append(int(inp()))
solutions = []

#Call function
equal_sum(total, lista, size-1, [], solutions)

#Output
for x in solutions[::-1]:
    st = f'{x}'
    clau = '{}'
    print(f'{clau[0]}{st[1:-1]}{clau[1]}')
