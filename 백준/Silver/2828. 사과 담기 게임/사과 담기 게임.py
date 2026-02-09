n, m = map(int, input().split())
j = int(input())

start, end = 1, m
min_d = 0

for _ in range(j):
    now = int(input())

    if now < start:
        d = start - now
        
        min_d += d
        start -= d
        end -= d

    elif now > end:
        d = now - end

        min_d += d
        start += d
        end += d

print(min_d)