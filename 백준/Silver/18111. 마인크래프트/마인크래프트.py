import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(n)]

min_h = min(map(min, ground))
max_h = max(map(max, ground))

best_time, best_height = int(1e9), 0 
for h in range(min_h, max_h+1):
    time, inventory = 0, b
    
    for row in range(n):
        for col in range(m):
            cur = ground[row][col]
            
            # 블록 제거
            if cur > h:
                diff = cur - h
                time += diff * 2
                inventory += diff
            
            # 블록 놓기
            elif cur < h:
                diff = h - cur
                time += diff
                inventory -= diff
                
    if inventory < 0:
        continue
    
    if time < best_time:
        best_time = time
        best_height = h
    
    elif time == best_time and h > best_height:
        best_height = h
        
print(best_time, best_height)