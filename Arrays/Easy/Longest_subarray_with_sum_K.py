def longest_subarray_sum(nums,key):
    longest = 0
    current_sum = 0
    prefix_sum = {}

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum == k:
            longest = i + 1

        if (current_sum - k) in prefix_sum:
            length = i - prefix_sum[current_sum - k]
            longest = max(longest, length)

        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i

    return longest

# Example usage:
nums = [10, 5, 2, 7, 1, 9]
k = 15
nums = [-3, 2, 1] 
k=6
print("Longest subarray length:", longest_subarray_sum(nums, k))
# Output → 4 (subarray is [5, 2, 7, 1])