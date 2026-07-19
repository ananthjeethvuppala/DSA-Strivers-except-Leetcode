s = input().strip()

values = {
    'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16
}

result = 0
power = 0
for ch in reversed(s):
    if ch.isdigit():
        val = int(ch)
    else:
        val = values[ch]
    result += val * (17 ** power)
    power += 1
print(result)
# --OR--
print(int(s,17))