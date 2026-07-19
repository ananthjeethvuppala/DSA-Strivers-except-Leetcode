def insertAtBottom(stack, element):
    if not stack:
        stack.append(element)
        return
    temp = stack.pop()
    insertAtBottom(stack, element)
    stack.append(temp)
    return

def reverseStack(stack):
    if len(stack) <= 1:
        return
    temp = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, temp)

# Input
n = int(input("Enter number of elements: "))
stack = list(map(int, input("Enter stack elements: ").split()))

reverseStack(stack)

print("Reversed Stack:")
print(stack)