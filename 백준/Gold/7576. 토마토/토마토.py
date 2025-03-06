import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while queue:
        x, y = queue.popleft()    

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i,j))

bfs()

max_days = 0
for row in tomatoes:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)
    max_days = max(max_days, max(row))

print(max_days-1)