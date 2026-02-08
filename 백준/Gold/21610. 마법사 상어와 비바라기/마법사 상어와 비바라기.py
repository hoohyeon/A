n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 방향 1 ~ 8
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 시작 구름
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

for _ in range(m):
    d, s = map(int, input().split())
    
    # 구름 이동
    new_clouds = []
    
    for r, c in clouds:
        nr = (r + dr[d] * s) % n
        nc = (c + dc[d] * s) % n
    
        new_clouds.append([nr, nc])
        
    clouds = new_clouds
    
    # 비 내리기
    for r, c in clouds:
        board[r][c] += 1
    
    # 물 복사 버그
    for r, c in clouds:
        cnt = 0
        for dir in [2, 4, 6, 8]:
            nr = r + dr[dir]
            nc = c + dc[dir]
    
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] > 0:
                    cnt += 1
                    
        board[r][c] += cnt
        
    # 기존 구름 위치 기록
    visited = [[False] * n for _ in range(n)]
    for r, c in clouds:
        visited[r][c] = True
        
    # 새 구름 생성
    clouds = []
    for r in range(n):
        for c in range(n):
            if board[r][c] >= 2 and not visited[r][c]:
                clouds.append([r, c])
                board[r][c] -= 2

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]
        
print(answer)