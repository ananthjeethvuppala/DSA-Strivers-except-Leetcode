def leaders(nums: list[int]) -> list[int]:
    leaders = []
    n = len(nums)
    max_from_right = float('-inf')

    for i in range(n-1, -1, -1):
        if nums[i] > max_from_right:
            leaders.append(nums[i])
            max_from_right = nums[i]
    leaders.reverse()
    return leaders

# Example 1
nums = [1, 2, 5, 3, 1, 2]
print(leaders(nums))  # Output: [5, 3, 2]

# Example 2
nums = [-3, 4, 5, 1, -4, -5]
print(leaders(nums))  # Output: [5, 1, -4, -5]