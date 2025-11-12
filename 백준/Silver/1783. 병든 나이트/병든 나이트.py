n, m = map(int, input().split())

cnt = 0
if n == 1:
    cnt = 1
    
elif n == 2:
    if 1 <= m <= 6:
        cnt = (m + 1) // 2
    
    else:
        cnt = 4

else:
    if 1 <= m <= 6:
        cnt = min(m, 4)

    else:
        cnt = m - 2

print(cnt)