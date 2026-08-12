# Infix to Prefix

# Problem Statement: Given an infix expression, Your task is to convert the given infix expression to a prefix expression.

def infixToprefix(s):
    stack = []
    result = []
    precedence = {'^': 3, '/': 2, '*': 2, '-': 1, '+': 1}
    
    s = s[::-1]
    for i in range(len(s)):

        if s[i] == "(":
            s = s[:i] + ")" + s[i+1:]
        elif s[i] == ")":
            s = s[:i] + "(" + s[i+1:]

    for ch in s:

        if ch.isalnum():
            result.append(ch)

        elif ch == "(":
            stack.append(ch)

        elif ch == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())

            stack.pop()

        else:
            while (stack and stack[-1] != "(" and (precedence[stack[-1]] > precedence[ch] or (precedence[stack[-1]] == precedence[ch] and ch == "^"))):
                result.append(stack.pop())

            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return "".join(result)[::-1]

# Input
expression = input("Enter infix expression: ")

# Conversion
prefix = infixToprefix(expression)

# Display
print("Infix Expression :", expression)
print("Prefix Expression:", prefix)