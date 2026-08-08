# Definition of Selection Sort:

# Selection Sort is a simple comparison-based sorting algorithm that works by repeatedly selecting the 
# smallest (or largest) element from the unsorted part of the array and swapping it with the element at 
# the beginning of the unsorted part.

# This process continues until the entire array is sorted.

# ⚡ In short:
# It divides the array into two parts – a sorted part (at the beginning) and an unsorted part (the rest). 
# On each pass, the smallest element from the unsorted part is placed into the correct position in the sorted part.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr