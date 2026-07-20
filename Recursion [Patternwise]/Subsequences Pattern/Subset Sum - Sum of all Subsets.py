def subSet(nums):
    ans = []

    def solve(index, currentsum):

        if index == len(nums):
            ans.append(currentsum)
            return
        
        solve(index + 1, currentsum + nums[index])

        solve(index + 1, currentsum)
    
    solve(0, 0)

    ans.sort()
    return ans

# Input
nums = list(map(int, input("Enter array elements: ").split()))

print("Answer =", subSet(nums))