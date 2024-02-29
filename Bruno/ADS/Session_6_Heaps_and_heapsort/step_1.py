def parent_index(idx):
    """
    Calculate the index of the parent element in a heap.

    Parameters:
    - idx: Index of the current element.

    Returns:
    Index of the parent element.
    """
    if idx == 0:
        return None  # No parent for the root element
    return (idx - 1) // 2

def left_child_index(idx):
    """
    Calculate the index of the left child element in a heap.

    Parameters:
    - idx: Index of the current element.

    Returns:
    Index of the left child element.
    """
    return 2 * idx + 1

def right_child_index(idx):
    """
    Calculate the index of the right child element in a heap.

    Parameters:
    - idx: Index of the current element.

    Returns:
    Index of the right child element.
    """
    return 2 * idx + 2

# Example usage:
index = 3  # Example index, change it as needed
parent_idx = parent_index(index)
left_child_idx = left_child_index(index)
right_child_idx = right_child_index(index)

#print("Index:", index)
#print("Parent Index:", parent_idx)
#print("Left Child Index:", left_child_idx)
#print("Right Child Index:", right_child_idx)



from heapq import heapify

# Example usage:
data = [4, 10, 3, 5, 1]
heapify(data)
print(data)

