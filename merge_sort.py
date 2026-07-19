# Definition of Merge Sort

# Merge Sort is a divide-and-conquer sorting algorithm that works by:

# Dividing the array into two halves,

# Recursively sorting each half, and

# Merging the two sorted halves into a single sorted array.

# 📌 In short:
# Merge Sort splits the array until each part has only one element, 
# then merges those parts back together in sorted order.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_side = arr[:mid]
        right_side = arr[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = j = k = 0
        
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1

    return arr
    
#Example
arr = [5,1,4,2,8]
print("sorted Array: ", merge_sort(arr))