r, c, q = map(int, input().split())
light = [list(map(int, input().split())) for _ in range(r)]
ps = [[0] * (c+1) for _ in range(r+1)]

# 2차원 배열 합
for i in range(1, r+1):
    for j in range(1, c+1):
        ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + light[i-1][j-1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    
    total = ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]
    
    cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
    
    print(total // cnt) 