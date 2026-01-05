import sys, heapq
input = sys.stdin.readline

t = 0
while True:
    n = int(input())
    
    if n == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    INF = int(1e9)
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = graph[0][0]
    
    pq = []
    heapq.heappush(pq, (graph[0][0], 0, 0))
    
    while pq:
        coin, x, y = heapq.heappop(pq)
        
        if x == n-1 and y == n-1:
            break
        
        if coin > dist[x][y]:
            continue
        
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy            
            
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            
            next_coin = coin + graph[nx][ny]
            
            if dist[nx][ny] > next_coin:
                dist[nx][ny] = next_coin
                
                heapq.heappush(pq, (next_coin, nx, ny))
            
    t += 1
    print(f'Problem {t}: {dist[n-1][n-1]}')