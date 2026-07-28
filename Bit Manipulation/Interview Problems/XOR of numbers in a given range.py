# Find XOR of numbers from L to R

# Problem Statement: Given two integers L and R. Find the XOR of the elements in the range [L , R].

def xor_upto(num):
    if num % 4 == 0:
        return num
    elif num % 4 == 1:
        return 1
    elif num % 4 == 2:
        return num + 1
    else:
        return 0

# num = int(input("Enter the Number: "))
# print(f"XOR upto number: {xor_upto(num)}")

l = int(input("Enter the start Number: "))
r = int(input("Enter the end Number: "))

print(f"XOR {l} to {r} numbers are: {xor_upto(r) ^ xor_upto(l - 1)}")