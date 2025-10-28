n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]

INF = 1e9
dist = [INF] * (n+1)

def bf(start):
    
    dist[start] = 0
    
    for i in range(n):
        
        for j in range(m):
            
            cur_node, next_node, cost = edges[j]
            
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + cost:
                dist[next_node] = dist[cur_node] + cost
                
                if i == n-1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
    
else:
    for i in range(2, n+1):
        if dist[i] != INF:
            print(dist[i])
        else:
            print(-1)