n, m = map(int, input().split())
picture = [[0] * 101 for _ in range(101)]

for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    
    for i in range(lx, rx+1):
        for j in range(ly, ry+1):
            picture[i][j] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if picture[i][j] > m:
            cnt += 1
            
print(cnt)