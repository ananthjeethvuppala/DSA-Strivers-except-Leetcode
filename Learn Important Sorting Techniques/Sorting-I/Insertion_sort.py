# Definition of Insertion Sort

# Insertion Sort is a simple comparison-based sorting algorithm in which
# elements are picked one by one from the unsorted part and inserted into
# their correct position in the sorted part of the array (usually on the left side).

# At each step, the algorithm takes the current element (called the key), 
# compares it with the already sorted elements, shifts the larger ones to 
# the right, and places the key in its proper position.

# 📌 In short:
# It works the same way we arrange playing cards in our hand — pick the 
# next card and insert it into the right place among the already sorted cards.


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

    return arr

#Example
arr = [5,1,4,2,8]
print("sorted Array: ", insertion_sort(arr))
