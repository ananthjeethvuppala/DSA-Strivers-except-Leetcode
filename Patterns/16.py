i = 0
j = 4
for row in range(7):
    for col in range(5):
        if col==0 or col==4-row or col==row-2:
            print("*",end="")
        else:
            print(end=" ")
    print()