# Check if a number is power of 2 or not

# Problem Statement: Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two if there exists an integer x such that n == 2ˣ.

n = int(input("Enter the Number: "))

if n > 0 and (n & (n - 1)) == 0:
    print("True")
else:
    print("False")