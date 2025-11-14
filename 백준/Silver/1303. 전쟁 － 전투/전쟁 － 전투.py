from collections import deque

n, m = map(int, input().split())

maps = [list(input()) for _ in range(m)]

def bfs(color):
    result = 0
    visit = [[0] * n for _ in range(m)]
    q = deque()

    for i in range(m):
        for j in range(n):
            if maps[i][j] != color:
                continue

            if not visit[i][j]:
                q.append((i, j))
                visit[i][j] = 1
                cnt = 1

                while q:
                    r, c = q.popleft()

                    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc

                        if not ((0 <= nr < m) and (0 <= nc < n)):
                            continue

                        if maps[nr][nc] != color:
                            continue

                        if not visit[nr][nc]:
                            q.append((nr, nc))
                            visit[nr][nc] = 1
                            cnt += 1

                result += cnt * cnt
        
    return result


print(bfs('W'), bfs('B'))