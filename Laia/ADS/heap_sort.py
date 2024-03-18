from heapq import heapify
from pytokr import pytokr

item, items = pytokr(iter = True)

### using heapify (petit --> gran)
def heap_sort_1(heap):
   result = []
   for j in range(len(heap)):
       heapify(heap)
       result.append(heap.pop(0))
   return result

### sense heapify (gran --> petit) (maxheap)
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

def sift_up(heap, index):
   while index >  0:
       parent_index = (index -  1) //  2
       if heap[parent_index] >= heap[index]:
           break
       heap[parent_index], heap[index] = heap[index], heap[parent_index]
       index = parent_index
   return heap

def heap_sort_2(heap):
   result = []
   for j in range(len(heap)):
       for i in range(len(heap) // 2 - 1, -1, -1):
           sift_down(heap, i)
       result.append(heap.pop(0))
   return result

### sense heapify (petit --> gran) (minheap)
def sift_down2(heap, index):
   left_child = 2 * index +1
   right_child = 2 * index +2
   largest = index
   if left_child < len(heap) and heap[left_child] < heap[largest]:
       largest = left_child
   if right_child < len(heap) and heap[right_child] < heap[largest]:
       largest = right_child
   if largest != index:
       heap[index], heap[largest] = heap[largest], heap[index]
       sift_down2(heap, largest)

def heap_sort_3(heap):
   result = []
   for j in range(len(heap)):
       for i in range(len(heap) // 2 - 1, -1, -1):
           sift_down2(heap, i)
       result.append(heap.pop(0))
   return result

heap = []
for x in items():
   heap.append(x)
heap1 = heap.copy()
heap2 = heap.copy()
heap3 = heap.copy()

result = heap_sort_1(heap1)
result2 = heap_sort_2(heap2)
result3 = heap_sort_3(heap3)

print('heapyfy:', result, 'maxheap:', result2, 'minheap:', result3)

