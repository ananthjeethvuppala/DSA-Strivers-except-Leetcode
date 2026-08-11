# Prefix to Infix Conversion

# Problem Statement: You are given a valid arithmetic expression in prefix notation. Your task is to convert it into a fully parenthesized infix expression.
# Prefix notation (also known as Polish notation) places the operator before its operands. In contrast, infix notation places the operator between operands.

# Your goal is to convert the prefix expression into a valid fully parenthesized infix expression.

def prefixToinfix(s):
    stack = []

    for ch in reversed(s):

        if ch.isalnum():
            stack.append(ch)

        else:
            operand1 = stack.pop()
            operand2 = stack.pop()

            expression = "(" + operand1 + ch + operand2 + ")"

            stack.append(expression)
    return stack[-1]

# Input
expression = input("Enter prefix expression: ")

# Conversion
infix = prefixToinfix(expression)

# Display
print("Prefix Expression :", expression)
print("Infix Expression  :", infix)