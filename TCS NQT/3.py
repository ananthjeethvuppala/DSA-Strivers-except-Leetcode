n = int(input())
floors = list(map(int, input().split()))
current = 0
time = 0
for f in floors:
    time += abs(current - f)*2 + 1
    current = f
print(time)