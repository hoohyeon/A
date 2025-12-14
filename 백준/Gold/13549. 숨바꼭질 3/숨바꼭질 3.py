from collections import deque
MAX = 100000

n, k = map(int, input().split())
dist = [0] * (MAX+1)
q = deque([n])

min_x = 0
while q:
    x = q.popleft()
    
    if x == k:
        min_x = dist[x]
        break
    
    # 작은 위치부터
    for nx in (x * 2, x - 1, x + 1):
        if 0 <= nx <= MAX and not dist[nx]:
            if nx == x * 2:
                dist[nx] = dist[x]
            else:
                dist[nx] = dist[x] + 1
            q.append(nx)
print(min_x)