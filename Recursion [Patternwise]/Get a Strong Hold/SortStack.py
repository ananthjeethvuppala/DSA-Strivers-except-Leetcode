def insertSorted(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
        return
    temp = stack.pop()
    insertSorted(stack, element)
    stack.append(temp)

def sortStack(stack):
    if len(stack) <= 1:
        return
    temp = stack.pop()
    sortStack(stack)
    insertSorted(stack, temp)



# Input
n = int(input("Enter number of elements: "))

stack = list(map(int, input("Enter stack elements: ").split()))

# Sort the stack
sortStack(stack)

# Output
print("Sorted Stack (Bottom -> Top):")
print(stack)

print("\nSorted Stack (Top -> Bottom):")
for i in range(len(stack) - 1, -1, -1):
    print(stack[i], end=" ")
