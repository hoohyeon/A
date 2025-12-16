from collections import deque

k = int(input())
w, h = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(h)]

# 원숭이, 말 이동 배열
monkey = [(-1, 0), (0, 1), (1, 0), (0, -1)]
horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

# visit[x][y][cnt] = 좌표 (x, y), 말 움직임 cnt번
visit = [[[False] * (k+1) for _ in range(w)] for _ in range(h)]
visit[0][0][0] = True

# 좌표 (0, 0), 말 0번, 거리 0
dq = deque([(0, 0, 0, 0)])

min_move = -1
while dq:
    x, y, cnt, dist = dq.popleft()
    
    # 도착
    if x == h-1 and y == w-1:
        min_move = dist
        break
    
    # 원숭이
    for dx, dy in monkey:
        nx, ny = x + dx, y + dy
        
        if (0 <= nx < h and 0 <= ny < w):
            if maps[nx][ny] == 0 and not visit[nx][ny][cnt]: 
                visit[nx][ny][cnt] = True
                dq.append((nx, ny, cnt, dist+1))
    
    # 말 (cnt+1)
    if cnt < k:
        for dx, dy in horse:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < h and 0 <= ny < w):
                if maps[nx][ny] == 0 and not visit[nx][ny][cnt+1]:
                    visit[nx][ny][cnt+1] = True
                    dq.append((nx, ny, cnt+1, dist+1))
                    
print(min_move)