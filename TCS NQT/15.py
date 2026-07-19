n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
count = 1
for i in range(1,n):
    if arr[i] > arr[i - 1]:
        count += 1
print(count)