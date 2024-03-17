#!/usr/bin/python3
import sys


def sift_up(heap, index):
   while index >  0:
       parent_index = (index -  1) //  2
       if heap[parent_index] >= heap[index]:
           break
       heap[parent_index], heap[index] = heap[index], heap[parent_index]
       index = parent_index
   return heap


def sift_down(heap, index):
   left_child = 2 * index +1
   right_child = 2 * index +2
   largest = index
   if left_child < len(heap) and heap[left_child] > heap[largest]:
       largest = left_child
   if right_child < len(heap) and heap[right_child] > heap[largest]:
       largest = right_child
   if largest != index:
       heap[index], heap[largest] = heap[largest], heap[index]
       sift_down(heap, largest)

def heap_sort(heap):
   result = []
   for j in range(len(heap)):
       for i in range(len(heap) // 2 - 1, -1, -1):
           sift_down(heap, i)
       result.append(heap.pop(0))
   return result

heap=sys.stdin.readline().strip("\n").split()

for x in range(len(heap)):
    heap[x]=int(heap[x])

result = heap_sort(heap)
print(result)

#################################################
#Using heapq module
from heapq import heapify, heappop


x=[2,1,6,3,9,4]
def heap_sort(heap):
    heapify(heap)
    out_ls=[]

    while heap:

        out_ls.append(heappop(heap))

    return out_ls


#print(heap_sort(x))

def clean_heapsort(heap):
    heapify(heap)
    out_ls=[]
    for _ in range(len(heap)):
        small=heap[0]

        for i in range(1, len(heap)):
            if heap[i]<small:
                small=heap[i]

        heap.remove(small)
        out_ls.append(small)
        heapify(heap)

    return out_ls

print(clean_heapsort(x))
