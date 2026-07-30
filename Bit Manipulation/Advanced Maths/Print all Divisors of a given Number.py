# Print all Divisors of a given Number

# Problem Statement: Given an integer N, return all divisors of N.
# A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.
from math import sqrt

def divisors(n):

    div = []

    for i in range(1, int(sqrt(n))):

        if n % i == 0:

            div.append(i)

            if i != n // i:
                div.append(n // i)
    div.sort()
    return div

n = int(input("Enter the Number: "))
print(f"The divisors of {n} are {divisors(n)}")