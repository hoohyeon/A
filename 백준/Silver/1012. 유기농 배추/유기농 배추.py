import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    queue = deque()

    queue.append((x, y))

    # 방문
    field[x][y] = 0

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and field[nx][ny] == 1:
                queue.append((nx, ny))
                field[nx][ny] = 0

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(t):
    m, n, k = map(int, input().split())

    field = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    
    cnt = 0

    for x in range(m):
        for y in range(n):
            if field[x][y] == 1:
                bfs(x, y)
                cnt += 1

    print(cnt)

