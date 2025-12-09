from collections import deque
from itertools import combinations

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

zeros = [(i, j) for i in range(n) for j in range(m) if maps[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if maps[i][j] == 2]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
max_safe = 0

def bfs():
    virus_map = [r[:] for r in maps]
    
    q = deque(virus)
    
    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if virus_map[nr][nc] == 1:
                continue

            if virus_map[nr][nc] == 0:
                virus_map[nr][nc] = 2
                q.append((nr, nc))

    safe = sum(row.count(0) for row in virus_map)
    
    return safe

for w1, w2, w3 in combinations(zeros, 3):
    r1, c1 = w1
    r2, c2 = w2
    r3, c3 = w3

    # 벽 세우기
    maps[r1][c1] = 1
    maps[r2][c2] = 1
    maps[r3][c3] = 1

    now_safe = bfs()
    max_safe = max(max_safe, now_safe)

    # 벽 되돌리기
    maps[r1][c1] = 0
    maps[r2][c2] = 0
    maps[r3][c3] = 0

print(max_safe)