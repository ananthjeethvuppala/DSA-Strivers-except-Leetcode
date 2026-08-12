# Postfix to Infix

# Problem Statement: Given a postfix expression (a string), convert it into an equivalent infix expression. The postfix expression is evaluated from left to right. The infix expression should have the proper parentheses to ensure correct operator precedence.
# Write a function to perform this conversion.

def postfixToinfix(s):
    stack = []

    for ch in s:

        if ch.isalnum():
            stack.append(ch)

        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            expression = "(" + operand1 + ch + operand2 + ")"

            stack.append(expression)

    return stack[-1]

# Input
expression = input("Enter postfix expression: ")

# Conversion
infix = postfixToinfix(expression)

# Display
print("Postfix Expression:", expression)
print("Infix Expression  :", infix)