from collections import deque

# m = row, n = col
m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
visit = [[False] * n for _ in range(m)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    # x = col, y = row
    for x in range(min(x1, x2), max(x1, x2)):
        for y in range(min(y1, y2), max(y1, y2)):
            graph[y][x] += 1

# 영역 넓이 반환
def bfs(sr, sc):
    area = 1
    q = deque([(sr, sc)])
    visit[sr][sc] = True
    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if (0 <= nr < m and 0 <= nc < n):
                if graph[nr][nc] == 0 and not visit[nr][nc]:
                    area += 1
                    visit[nr][nc] = True                    
                    q.append((nr, nc))
    return area
    
cnt = 0
areas = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visit[i][j]:
            area = bfs(i, j)
            areas.append(area)
            cnt += 1

# 영역 개수 = bfs 함수 실행 횟수
# 영역 넓이 = bfs 함수 반환 값
print(cnt)
print(*sorted(areas))