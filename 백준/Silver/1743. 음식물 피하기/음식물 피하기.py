import sys
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, input().split())
grid = [['.'] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    grid[r-1][c-1] = '#'
    
visit = [[False] * m for _ in range(n)]

def dfs(sr, sc):

    visit[sr][sc] = True
    cnt = 1
            
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = sr + dr, sc + dc
        
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        
        if not grid[nr][nc] == '#':
            continue
            
        if visit[nr][nc]:
            continue
        
        visit[nr][nc] = True
        cnt += dfs(nr, nc)
            
    return cnt

max_cnt = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' or visit[i][j]:
            continue
        
        max_cnt = max(max_cnt, dfs(i, j))

print(max_cnt)