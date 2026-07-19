N = int(input())
arr = list(map(int, input().split()))
D = int(input())
x = int(input())

even = odd = 0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
if D % 2 == 0:
    print(odd*x)
else:
    print(even*x)
