from pytokr import pytokr

s = pytokr()

def subsets_helper(words, current, index):
    if index == len(words):
        print('{' + ', '.join(current) + '}' if current else '{}')
        return

    # Exclude
    subsets_helper(words, current, index + 1)

    # Include the current word in the subset
    subsets_helper(words, current + [words[index]], index + 1)

def subsets(words):
    subsets_helper(words, [], 0)


n = int(s())
words = []

for _ in range(n):
    word = s().strip()
    words.append(word)

words_sorted = sorted(words, reverse=True)


subsets(words_sorted)





