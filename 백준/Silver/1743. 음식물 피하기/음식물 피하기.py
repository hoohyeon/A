from collections import deque

n, m, k = map(int, input().split())
grid = [['.'] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    grid[r-1][c-1] = '#'
    
visit = [[False] * m for _ in range(n)]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visit[sr][sc] = 1
    cnt = 1
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            
            if not grid[nr][nc] == '#':
                continue
                
            if visit[nr][nc]:
                continue
            
            visit[nr][nc] = True
            q.append((nr, nc))
            cnt += 1
            
    return cnt

max_cnt = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            continue
        max_cnt = max(max_cnt, bfs(i, j))
        
print(max_cnt)    