from collections import deque

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
person = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'I':
            sr, sc = i, j

visited[sr][sc] = 1
q = deque([(sr,sc)])

while q:
    r, c = q.popleft()
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc

        # 1) 범위 밖
        if not (0 <= nr < n and 0 <= nc < m):
            continue

        # 2) 벽
        if maps[nr][nc] == 'X':
            continue

        # 3) 이미 방문
        if visited[nr][nc]:
            continue

        visited[nr][nc] = 1
        if maps[nr][nc] == 'P':
            person += 1
        
        q.append((nr, nc))

print('TT' if person == 0 else person)