from collections import deque

n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]

# 최대 높이
max_h = max(map(max, height))

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(sr, sc, rain):
    
    q = deque([(sr, sc)])
    
    visit[sr][sc] = True
    
    while q:
    
        r, c = q.popleft()
    
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            
            if height[nr][nc] <= rain:
                continue
            
            if visit[nr][nc]:
                continue

            visit[nr][nc] = True
            q.append((nr, nc))

max_cnt = 0
for h in range(max_h + 1):
    visit = [[False] * n for _ in range(n)]
    
    cnt = 0
    for i in range(n):
        for j in range(n):        
            if height[i][j] > h and not visit[i][j]:
                bfs(i, j, h)
                cnt += 1
                
    max_cnt = max(max_cnt, cnt)
               
print(max_cnt)