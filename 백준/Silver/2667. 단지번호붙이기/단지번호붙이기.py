from collections import deque

n = int(input())

maps = [list(map(int, input())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    visited[x][y] = village
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = village
                    queue.append((nx, ny))
    
village = 1

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            village += 1

village -= 1
print(village)

result = [0] * village

for i in range(1, village + 1):
    for row in visited:
        result[i-1] += row.count(i)

result.sort()

for r in result:
    print(r)