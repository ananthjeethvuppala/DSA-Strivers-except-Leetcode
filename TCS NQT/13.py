start = input().strip().lower()
n = int(input())

days = {
    'sun':0, 'mon':1, "tue":2, 'wed':3, 'thr':4, 'fri':5, 'sat':6
}

day = days[start]
first_sunday = (7 - day) % 7
count = 0
if first_sunday < n:
    count = 1
    remain = n - first_sunday
    count += remain // 7
print(count)