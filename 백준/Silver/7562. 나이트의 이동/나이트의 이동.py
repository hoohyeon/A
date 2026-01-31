import sys
input = sys.stdin.readline

from collections import deque

t = int(input())

for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    
    dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    
    cnt = [[-1] * l for _ in range(l)]
    cnt[sx][sy] = 0
    
    min_cnt = 0
    
    q = deque([(sx, sy)])
    
    while q:
        cx, cy = q.popleft()
        
        if cx == gx and cy == gy:
            min_cnt = cnt[cx][cy]
            break
        
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            
            if not (0 <= nx < l and 0 <= ny < l):
                continue
            
            if cnt[nx][ny] == -1:
                cnt[nx][ny] = cnt[cx][cy] + 1
                q.append((nx, ny))
    
    print(min_cnt)