from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            start = (i, j)
            dist[i][j] = 0
            
queue = deque([start])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    
bfs()

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()