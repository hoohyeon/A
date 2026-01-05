import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
    
INF = int(1e9)
def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_cost, cur = heapq.heappop(pq)
        
        if dist[cur] < cur_cost:
            continue
        
        for nxt, weight in graph[cur]:
            nxt_cost = cur_cost + weight
            
            if dist[nxt] > nxt_cost:
                dist[nxt] = nxt_cost
                
                heapq.heappush(pq, (nxt_cost, nxt))
                
    return dist

# 모든 점에서 최소 거리 배열
# 해당 배열에서 얻을 수 있는 아이템 개수 cnt
# 각 점마다 max_cnt 갱신
max_cnt = 0
for i in range(1, n+1):
    dist = dijkstra(i)
    
    cnt = 0
    for j in range(1, n+1):
        if dist[j] <= m:
            cnt += items[j-1]
    max_cnt = max(max_cnt, cnt)
    
print(max_cnt)