# Count the number of set bits

# Problem Statement: Given an integer n, return the number of set bits (1s) in its binary representation.
# Can you solve it in O(log n) time complexity?

n = int(input("Enter a Number: "))

count = 0

while n > 0:
    if n & 1 == 1:
        count += 1
    n = n >> 1

print(count)