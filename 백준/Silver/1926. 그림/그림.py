from collections import deque

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y):
    q = deque([(x, y)])
    visit[x][y] = True
    area = 1
    
    while q:
        cx, cy = q.popleft()

        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            
            # 도화지 안에
            if 0 <= nx < n and 0 <= ny < m:
                
                # 그림이고 연결 X
                if picture[nx][ny] == 1 and not visit[nx][ny]:        
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    area += 1
    return area

cnt, max_area = 0, 0
for row in range(n):
    for col in range(m):
        if picture[row][col] == 1 and not visit[row][col]:
            # 그림 개수
            cnt += 1
            
            # 이번 그림 넓이
            area = bfs(row, col)

            # 최대 그림 넓이 갱신
            max_area = max(max_area, area)

print(cnt)
print(max_area)