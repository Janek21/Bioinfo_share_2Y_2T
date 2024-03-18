from heapq import heapify

def sift_up(heap, i):
    parent = (i - 1) // 2 # get the index of the parent
    while i > 0 and heap[i] < heap[parent]: # if heap at the current index is smaller than the parent
        heap[i], heap[parent] = heap[parent], heap[i] # swap them
        i = parent # actualize the index bc our item is now on the parent's index
        parent = (i - 1) // 2 # get another index for the parent

data = [5, 4, 3, 2, 1, 0]
data2 = [5, 4, 3, 2, 1, 0]

heapify(data)
print(data)

sift_up(data2, len(data2)-1)
print(data2)


############### no va:)