from collections import deque

m, n = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# dist[x][y] = (x, y) 까지의 최소 비용
INF = 10**9
dist = [[INF] * m for _ in range(n)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

dq = deque([(0, 0)])
dist[0][0] = 0
while dq:
    x, y = dq.popleft()

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        # 유효 좌표
        if (0 <= nx < n and 0 <= ny < m):
            # 새로운 경로가 비용이 더 낮으면
            if dist[nx][ny] > dist[x][y] + maze[nx][ny]:
                dist[nx][ny] = dist[x][y] + maze[nx][ny]
                # 빈 방 = 0
                if maze[nx][ny] == 0:
                    dq.appendleft((nx, ny))
                # 벽 = 1
                else:
                    dq.append((nx, ny))

print(dist[n-1][m-1])