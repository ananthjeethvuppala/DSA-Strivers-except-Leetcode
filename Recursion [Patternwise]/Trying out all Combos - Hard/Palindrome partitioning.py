def palindromePartition(s):

    ans = []
    path = []

    def isPallindrome(substring):
        return substring == substring[::-1]
    
    def solve(index):

        if index == len(s):
            ans.append(path.copy())
            return
        
        for end in range(index, len(s)):

            substring = s[index:end + 1]

            if not isPallindrome(substring):
                continue

            path.append(substring)

            solve(end + 1)

            path.pop()

    solve(0)
    return ans

# Input
s = input("Enter the string: ")

print("Palindrome Partitions:")
print(palindromePartition(s))