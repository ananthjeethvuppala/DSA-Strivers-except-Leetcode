a = int(input())
bits = len(bin(a)) - 2
mask = (1 << bits) - 1

print(a^mask)
