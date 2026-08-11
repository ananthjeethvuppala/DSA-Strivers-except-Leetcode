# Postfix to Prefix Conversion

# Problem Statement: You are given a valid postfix expression as a string, where:
# Operands are single lowercase English letters ('a' to 'z')
# Operators are binary: '+', '-', '*', '/'
# The expression contains no spaces and is guaranteed to be valid.

# Write a function to convert the postfix expression into a prefix expression, also as a string without spaces.

def postfixToprefix(s):

    stack = []

    for ch in s:

        if ch.isalnum():
            stack.append(ch)

        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            expression = ch + operand1 + operand2

            stack.append(expression)

    return stack[-1]

# Input
expression = input("Enter postfix expression: ")

# Conversion
prefix = postfixToprefix(expression)

# Display
print("Postfix Expression:", expression)
print("Prefix Expression :", prefix)