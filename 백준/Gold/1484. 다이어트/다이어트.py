g = int(input())

a = 1
b = 2

ans = []
while b <= 100000:

    diff = b ** 2 - a ** 2

    if diff == g:
        ans.append(b)
        b += 1

    elif diff > g:
        a += 1

    else:
        b += 1

if ans:
  print(*ans)

else:
  print(-1)