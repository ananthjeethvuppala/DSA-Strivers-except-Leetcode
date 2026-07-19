a = list(map(int, input().split()))
even = 0
suma = 0
for num in a:
    if num % 2 == 0:
        even += 1
for num in a:
    suma += num
unique = set(a) == 4

if even % 2 ==0 and unique and suma % 3 == 0:
    print('OPEN')
else:
    print('LOCKED')

