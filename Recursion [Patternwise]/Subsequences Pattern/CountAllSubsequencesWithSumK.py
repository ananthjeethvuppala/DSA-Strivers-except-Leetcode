def countSubsequences(nums, k):

    def solve(index, currsum):

        if index == len(nums):
            if currsum == k:
                return 1
            return 0
        
        take = solve(index + 1, currsum + nums[index])
        skip = solve(index + 1, currsum)

        return take + skip
    
    return solve(0, 0)

# Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

print("Count =", countSubsequences(nums, k))