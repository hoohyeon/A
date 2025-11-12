n, m = map(int, input().split())

lamps = [input() for _ in range(n)]

k = int(input())

max_cnt = 0
for lamp in lamps:

    off_lamp = lamp.count('0')

    if off_lamp <= k and (k - off_lamp) % 2 == 0:
        cnt = lamps.count(lamp)

        max_cnt = max(max_cnt, cnt)

print(max_cnt)