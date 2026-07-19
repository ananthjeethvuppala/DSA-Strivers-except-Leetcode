# n = input()
# prod = 1
# for ch in n:
#     prod *= int(ch)
# print(prod)
n = int(input())
prod = 1
digit = 0
while n > 0:
    digit = n % 10
    prod *= digit
    n = n // 10
print(prod)
