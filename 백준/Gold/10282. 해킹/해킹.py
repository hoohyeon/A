import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
        
    dist = [INF] * (n+1)
    dist[c] = 0
    
    pq = [(0, c)]
    
    while pq:
        cur_dist, cur = heapq.heappop(pq)
        
        if cur_dist > dist[cur]:
            continue
        
        for next_node, cost in graph[cur]:
            next_dist = cur_dist + cost
            if dist[next_node] > next_dist:
                dist[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))
    
    cnt, time = 0, 0
    
    for d in dist[1:]:
        if d != INF:
            cnt += 1
            time = max(d, time)
        
    print(cnt, time)