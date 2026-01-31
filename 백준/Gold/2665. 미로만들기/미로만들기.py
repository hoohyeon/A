from collections import deque

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]

dist = [[-1] * n for _ in range(n)]
dist[0][0] = 0

q = deque([(0, 0)])

while q:
    cx, cy = q.popleft()
    
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = cx + dx, cy + dy
        
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        
        # 이미 방문한 방
        if dist[nx][ny] != -1:
            continue
        
        # 흰 방
        if maps[nx][ny] == 1:
            dist[nx][ny] = dist[cx][cy]
            q.appendleft((nx, ny))
        
        # 검은 방
        else:
            dist[nx][ny] = dist[cx][cy] + 1
            q.append((nx, ny))

print(dist[n-1][n-1])