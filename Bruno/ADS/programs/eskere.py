def find_subsets_with_sum(s, n, numbers):
    def backtrack(start, target, current_subset):
        if target == 0:
            result.append(current_subset.copy())
            return

        for i in range(start, n):
            if target - numbers[i] >= 0:
                current_subset.append(numbers[i])
                backtrack(i + 1, target - numbers[i], current_subset)
                current_subset.pop()

    result = []
    backtrack(0, s, [])

    for subset in result:
        print(subset)

# Input
s = int(input())
n = int(input())
numbers = list(map(int, input().split()))

# Output
find_subsets_with_sum(s, n, numbers)
