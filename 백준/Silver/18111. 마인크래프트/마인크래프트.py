n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

h_count = [0] * 257
for row in range(n):
    for col in range(m):
        height = ground[row][col]
        h_count[height] += 1

min_h = min(i for i in range(257) if h_count[i] > 0)
max_h = max(i for i in range(257) if h_count[i] > 0)

best_time, best_height = int(1e9), 0 
for target_h in range(min_h, max_h+1):
    time, inventory = 0, b

    for cur_h in range(min_h, max_h+1):
        cnt = h_count[cur_h]
        
        if cnt == 0:
            continue
    
        # 블록 제거
        if cur_h > target_h:
            diff = cur_h - target_h
            time += diff * 2 * cnt
            inventory += diff * cnt
            
        elif cur_h < target_h:
            diff = target_h - cur_h
            time += diff * cnt
            inventory -= diff * cnt
        
    if inventory < 0:
        continue
    
    if time < best_time:
        best_time = time
        best_height = target_h
    
    elif time == best_time and target_h > best_height:
        best_height = target_h
            
print(best_time, best_height)