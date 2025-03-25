n = int(input())

meeting = [tuple(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x:(x[1], x[0]))

cnt = 0
start, end = 0, 0

for m in meeting:
    next_start, next_end = m

    if next_start >= end:
        cnt += 1
        end = next_end

print(cnt)