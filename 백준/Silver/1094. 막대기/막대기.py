n = int(input())

stick = 64
cnt = 0

while n > 0:
    if n >= stick:
        n -= stick
        cnt += 1

    else:
        stick //= 2


print(cnt)