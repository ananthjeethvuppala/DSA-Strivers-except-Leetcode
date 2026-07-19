s = input().strip()
l = int(input().strip())
max_count = 0

for i in range(0,len(s),l):
    substring = s[i:i+l]
    count_a = substring.count('a')
    max_count = max(max_count,count_a)
print(max_count)