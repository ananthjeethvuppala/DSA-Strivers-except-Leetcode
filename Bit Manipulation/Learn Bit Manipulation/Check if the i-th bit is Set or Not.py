n = int(input("Enter the Number: "))
i = int(input("Enter the bit position: "))

if (n >> i) & i:
    print("True")
else:
    print("False")