# Next Smaller Element

# Problem Statement: Given an array of integers arr, your task is to find the Next Smaller Element (NSE) for every element in the array.
# The Next Smaller Element for an element x is defined as the first element to the right of x that is smaller than x.
# If there is no smaller element to the right, then the NSE is -1.

def nextSmallerElement(nums):
    n = len(nums)
    stack = []
    result = [-1] * n

    for i in range(n-1, -1, -1):

        current = nums[i]
        while stack and stack[-1] >= current:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(current)

    return result

# Input
arr = list(map(int, input("Enter array elements: ").split()))

# Conversion
result = nextSmallerElement(arr)

# Display
print("Input Array :", arr)
print("NSE Array   :", result)