a = int(input())
x, y = 0, 0
distance = 10

for i in range(1,a+1):
    if i % 4 == 1:
        x += distance
    elif i % 4 == 2:
        y += distance
    elif i % 4 == 3:
        x -= distance
    elif i % 4 == 0:
        x -= distance
    distance += 10

print(x,y)