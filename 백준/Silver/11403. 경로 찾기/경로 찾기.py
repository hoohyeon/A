n = int(input())

g = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        
        if g[i][k] == 0:
            continue
        
        for j in range(n):

            if g[i][j] == 1:
                continue

            if g[k][j]:
                g[i][j] = 1
                
for row in g:
    print(*row)