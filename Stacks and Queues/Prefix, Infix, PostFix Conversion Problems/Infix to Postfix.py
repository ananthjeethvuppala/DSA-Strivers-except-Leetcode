# Infix to Postfix

# Problem Statement: Given an infix expression, Your task is to convert the given infix expression to a postfix expression.

def infixToPostfix(s):
    result = []
    stack = []
    precedence = {'^': 3, '/': 2, '*': 2, '-': 1, '+': 1}

    for ch in s:

        if ch.isalnum():
            result.append(ch)

        elif ch == "(":
            result.append(ch)

        elif ch == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())

        else:
            while (stack and stack[-1] != '(' and (precedence[stack[-1]] > precedence[ch] or (precedence[stack[-1]] == precedence[ch]) and ch == '^')):
                result.append(stack.pop())
            stack.append(ch)

        while stack:
            result.append(stack.pop())

    return ''.join(result)

# Input
expression = input("Enter infix expression: ")

# Convert
postfix = infixToPostfix(expression)

# Display
print("Infix Expression :", expression)
print("Postfix Expression:", postfix)