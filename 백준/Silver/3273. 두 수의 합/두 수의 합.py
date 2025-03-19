n = int(input())

numbers = sorted(list(map(int, input().split())))

x = int(input())

cnt = 0
left, right = 0, n-1

while left < right:
    temp = numbers[left] + numbers[right]

    if temp == x:
        cnt += 1
        left += 1

    elif temp < x:
        left += 1
    
    elif temp > x:
        right -= 1


print(cnt)