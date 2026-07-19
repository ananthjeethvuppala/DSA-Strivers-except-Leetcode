def existsSubsequence(nums, k):

    def solve(index, currentsum):

        if index == len(nums):
            if currentsum == k:
                return True
            return False
        
        take = solve(index + 1, currentsum + nums[index])
        skip = solve(index + 1, currentsum)

        return take or skip
    
    return solve(0, 0)


# Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

if existsSubsequence(nums, k):
    print("Yes")
else:
    print("No")