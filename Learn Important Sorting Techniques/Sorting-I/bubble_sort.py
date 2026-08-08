# Definition of Bubble Sort

# Bubble Sort is a simple comparison-based sorting algorithm in which adjacent elements
# are compared and swapped if they are in the wrong order.

# This process is repeated for multiple passes until the array becomes sorted. After each
#  pass, the largest element of the unsorted portion “bubbles up” to its correct position
# at the end of the array.

# 📌 In short:
# Bubble Sort keeps swapping neighboring elements until no swaps are needed, meaning the
# array is sorted.

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

#Example
arr = [5,1,4,2,8]
print("sorted Array: ", bubble_sort(arr))


# step-by-step debug (dry run) of Bubble Sort on
# arr = [5, 1, 4, 2, 8] using the optimized version (with swapped flag).

# Pass 1 (i = 0) — start: [5, 1, 4, 2, 8]
# j	Compare	Action	Array after
# 0	(5, 1)	swap	[1, 5, 4, 2, 8]
# 1	(5, 4)	swap	[1, 4, 5, 2, 8]
# 2	(5, 2)	swap	[1, 4, 2, 5, 8]
# 3	(5, 8)	no swap	[1, 4, 2, 5, 8]

# End of Pass 1: largest (8) bubbled to the end.

# Pass 2 (i = 1) — start: [1, 4, 2, 5, 8]
# j	Compare	Action	Array after
# 0	(1, 4)	no swap	[1, 4, 2, 5, 8]
# 1	(4, 2)	swap	[1, 2, 4, 5, 8]
# 2	(4, 5)	no swap	[1, 2, 4, 5, 8]

# End of Pass 2: next largest (5) in place.

# Pass 3 (i = 2) — start: [1, 2, 4, 5, 8]
# j	Compare	Action	Array after
# 0	(1, 2)	no swap	[1, 2, 4, 5, 8]
# 1	(2, 4)	no swap	[1, 2, 4, 5, 8]

# No swaps this pass → already sorted. Algorithm stops early.

# Final sorted array

# [1, 2, 4, 5, 8]