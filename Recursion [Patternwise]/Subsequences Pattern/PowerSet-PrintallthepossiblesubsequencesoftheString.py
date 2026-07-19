def generateSubsequences(s):
    ans = []

    def solve(index, curr):

        if index == len(s):
            if curr != '':
                ans.append(curr)
            return
        
        solve(index + 1, curr + s[index])

        solve(index + 1, curr)

    solve(0,"")

    return ans

# Input
s = input("Enter a string: ")

# Output
print(generateSubsequences(s))