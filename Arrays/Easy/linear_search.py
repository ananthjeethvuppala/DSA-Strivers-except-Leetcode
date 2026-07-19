def findIndex(nums, target) -> None:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Example 1
nums1 = [2, 3, 4, 5, 3]
target1 = 3
print(findIndex(nums1, target1))  # Output: 1

# Example 2
nums2 = [2, -4, 4, 0, 10]
target2 = 6
print(findIndex(nums2, target2))  # Output: -1