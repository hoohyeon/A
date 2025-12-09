from collections import deque

n = int(input())

grid_normal = [input() for _ in range(n)]
grid_blind = [list(row.replace('G', 'R')) for row in grid_normal]

visit_normal = [[False] * n for _ in range(n)]
visit_blind = [[False] * n for _ in range(n)]

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y, grid, visit):
    q = deque([(x, y)])
    visit[x][y] = True

    while q:
        r, c = q.popleft()
    
        for dr, dc in d:
            nr, nc = r + dr, c + dc
    
            if not (0 <= nr < n and 0 <= nc < n):
                continue
    
            if (grid[r][c] != grid[nr][nc]):
                continue
    
            if not visit[nr][nc]:
                visit[nr][nc] = True
                q.append((nr, nc))
                
normal_cnt = 0
for i in range(n):
    for j in range(n):
        if not visit_normal[i][j]:
            bfs(i, j, grid_normal, visit_normal)
            normal_cnt += 1

blind_cnt = 0
for i in range(n):
    for j in range(n):
        if not visit_blind[i][j]:
            bfs(i, j, grid_blind, visit_blind)
            blind_cnt += 1
            
print(normal_cnt, blind_cnt)