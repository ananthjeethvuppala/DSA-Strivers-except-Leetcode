N = int(input())
arr = list(map(int,input().split()))

if N % 2 != 0:
    print(-1)
else:
    total_sum = sum(arr)
    pairs = N // 2

    if total_sum % pairs != 0:
        print(-1)
    else:
        target = total_sum // pairs

        arr.sort()

        left = 0
        right = N-1
        count = 0
        possible = True

        while left < right:
            if arr[left] + arr[right] == target:
                count += 1
                left += 1
                right -= 1
            else:
                possible = False
                break
        if possible:
            print(count)
        else:
            print(-1)