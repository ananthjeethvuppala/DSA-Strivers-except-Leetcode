# Recursive Bubble Sort
# Idea

# In normal bubble sort, we keep running loops until the largest element bubbles to the end.

# In recursive bubble sort, we:

# Do one full pass (largest element moves to the end).

# Then recursively call bubble sort on the remaining n-1 elements.

# Base case → when array size is 1, it’s already sorted.

def recursive_bubble_sort(arr,n = None):
    if n == None:
        n = len(arr)

    if n == 1:
        return arr
    
    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

    return recursive_bubble_sort(arr,n-1)


# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original:", arr)
sorted_arr = recursive_bubble_sort(arr,)
print("Sorted:", sorted_arr)