import sys
input = sys.stdin.readline

from collections import deque

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
zero = 0

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                q.append((z, y, x))
            elif box[z][y][x] == 0:
                zero += 1

if zero == 0:
    print(0)

else:
    while q:
        cz, cy, cx = q.popleft()
    
        for i in range(6):
            nz, ny, nx = cz + dz[i], cy + dy[i], cx + dx[i]
    
            if not (0 <= nx < m and 0 <= ny < n and 0 <= nz < h):
                continue
    
            if box[nz][ny][nx] != 0:
                continue
    
            box[nz][ny][nx] = box[cz][cy][cx] + 1
            zero -= 1
    
            q.append((nz, ny, nx))
    
    if zero > 0:
        print(-1)
    
    else:
        max_day = 0
        for z in range(h):
            for y in range(n):
                max_day = max(max_day, max(box[z][y]))
        
        print(max_day - 1)