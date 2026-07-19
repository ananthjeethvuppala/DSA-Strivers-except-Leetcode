s = input().strip()
result = ''
i = 0
while i < len(s):
    if s[i].isdigit():
        num = int(s[i])
        char = s[i+1]
        for _ in range(num):
            result += char
        i += 2
    else:
        result += s[i]
        i += 1
print(result)