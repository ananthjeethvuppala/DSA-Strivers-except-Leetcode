n = int(input())
arr = list(map(int, input().split()))
pos = 0
for i in range(0,n):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1
for i in range(pos,n):
    arr[i] = 0
print(*arr)
print(arr)