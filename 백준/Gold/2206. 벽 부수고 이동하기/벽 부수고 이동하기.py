import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

# visited[r][c][broke] : (r, c)에 도착했을 때의 최단 거리
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

q = deque()
q.append((0, 0, 0))
visit[0][0][0] = 1

# 최단 거리 초기화
min_d = -1
while q:
    r, c, broke = q.popleft()

    # BFS - 도착하면 최단 거리
    if r == n-1 and c == m-1:
        min_d = visit[r][c][broke]
        break
    
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if not (0 <= nr < n and 0 <= nc < m):
            continue

        # 빈 칸으로 이동
        if board[nr][nc] == 0 and visit[nr][nc][broke] == 0:
            visit[nr][nc][broke] = visit[r][c][broke] + 1
            q.append((nr, nc, broke))

        # 벽 부수고 이동 
        if board[nr][nc] == 1 and broke == 0 and visit[nr][nc][1] == 0:
            visit[nr][nc][1] = visit[r][c][0] + 1
            q.append((nr, nc, 1))

print(min_d)