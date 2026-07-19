def generateBinaryStrings(n):
    ans = []

    def solve(curr):
        
        if len(curr) == n:
            ans.append(curr)
            return
        
        if curr == '':
            solve(curr + '0')
            solve(curr + '1')

        elif curr[-1] == "1":
            solve(curr + '0')

        else:
            solve(curr + '0')
            solve(curr + '1')
    solve("")
    return ans

# Input
n = int(input("Enter n: "))

# Function call
result = generateBinaryStrings(n)

# Output
print("Binary strings without consecutive 1s:")
print(result)