n = int(input())

calendar = [0] * 366

for _ in range(n):
    s, e = map(int, input().split())

    for i in range(s, e+1):
        calendar[i] += 1

width, height = 0, 0
area = 0
for c in calendar:

    if c > 0:
        width += 1
        height = max(height, c)

    else:
        area += width * height
        width, height = 0, 0
    
if width > 0:
    area += width * height

print(area)