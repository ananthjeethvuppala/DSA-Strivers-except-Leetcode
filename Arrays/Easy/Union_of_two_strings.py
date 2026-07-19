class Solution:
    def unionArrays(self,num1,num2):
        i = j = 0
        result = []

        while i < len(num1) and j < len(num2):
            if num1[i] == num2[j]:
                if not result or result[-1] != num1[i]:
                    result.append(num1[i])
                i += 1
                j += 1

            elif num1[i] < num2[j]:
                if not result or result[-1] != num1[i]:
                    result.append(num1[i])
                i += 1

            else:
                if not result or result[-1] != num2[j]:
                    result.append(num2[j])
                j += 1

        while i < len(num1):
            if not result or result[-1] != num1[i]:
                result.append(num1[i])
            i += 1

        while j < len(num2):
            if not result or result[-1] != num2[j]:
                result.append(num2[j])
            j += 1

        return result
    
sol = Solution()
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
print(sol.unionArrays(nums1, nums2))  
# Output: [1, 2, 3, 4, 5, 7]

nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]
print(sol.unionArrays(nums1, nums2))
# Output: [1, 3, 4, 5, 6, 7, 8, 9]