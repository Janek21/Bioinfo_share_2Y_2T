def sift_up(heap):
    idx = len(heap) - 1  #Index of the last inserted element
    while idx > 0:
        parent_idx = (idx - 1) // 2  #Calculate parent index
        if heap[parent_idx] > heap[idx]:
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            idx = parent_idx
        else:
            break
    return heap

# Example usage:
heap = [4, 10, 3, 5, 1]
print(heap)
sift_up(heap)
print(heap)
