# Definition of Quick Sort

# Quick Sort is a divide and conquer sorting algorithm that works by:

# Choosing a pivot element from the array.

# Partitioning the array so that all elements smaller than the pivot are 
# placed on the left, and all elements greater than the pivot are placed on the right.

# Recursively applying the same process to the left and right subarrays 
# until the entire array is sorted.

# ✅ Time Complexity:

# Best & Average Case: O(n log n)

# Worst Case (bad pivot choice): O(n²)

# ✅ Space Complexity:

# O(log n) (due to recursion stack).


def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

    return arr


# 🔹 Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)

sorted_arr = quick_sort(arr, 0, len(arr)-1)
print("Sorted array:", sorted_arr)