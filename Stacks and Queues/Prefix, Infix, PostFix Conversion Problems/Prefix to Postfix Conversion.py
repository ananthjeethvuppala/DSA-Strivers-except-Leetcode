# Prefix to Postfix Conversion

# Problem Statement: You are given a valid prefix expression consisting of binary operators and single-character operands. Your task is to convert it into a valid postfix expression.

# Prefix (Polish) notation places the operator before operands.
# Postfix (Reverse Polish) notation places the operator after operands.

def prefixTopostfix(s):
    stack = []

    for ch in reversed(s):

        if ch.isalnum():
            stack.append(ch)

        else:
            operand1 = stack.pop()
            operand2 = stack.pop()

            expression = operand1 + operand2 + ch

            stack.append(expression)

    return stack[-1]

# Input
expression = input("Enter prefix expression: ")

# Conversion
postfix = prefixTopostfix(expression)

# Display
print("Prefix Expression :", expression)
print("Postfix Expression:", postfix)