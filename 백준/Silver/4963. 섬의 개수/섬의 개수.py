from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visit[x][y] = True

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if (0 <= nr < h and 0 <= nc < w):
                if graph[nr][nc] == 1 and not visit[nr][nc]:
                    visit[nr][nc] = True
                    q.append((nr, nc))

while True:
    w, h = map(int, input().split())

    # 종료 조건
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    visit = [[False] * w for _ in range(h)]

    # 가로, 세로, 대각선
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, -1), (1, 0), (1, 1), (0, -1)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visit[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)