# Set the rightmost bit

# Problem Statement: Given a positive integer n, set the rightmost unset (0) bit of its binary representation to 1 and return the resulting integer.
# If all bits are already set, return the number as it is.

n = int(input("Enter the Number: "))

if (n & (n + 1)) == 0:
    print(n)
else:
    print(n | (n + 1))