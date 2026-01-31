import sys, heapq
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    
    graph[a].append((b, t))
    graph[b].append((a, t))

dist = [INF] * n
dist[0] = 0

# (거리, 노드)
pq = []
heapq.heappush(pq, (0, 0))

while pq:
    cur_dist, cur = heapq.heappop(pq)
    
    if cur_dist > dist[cur]:
        continue
    
    for nxt, cost in graph[cur]:
        # 갈 수 없는 곳 : 시야에 보이는 곳 (도착지 제외)
        if A[nxt] == 1 and nxt != n-1:
            continue
            
        nxt_dist = cur_dist + cost
        
        if dist[nxt] > nxt_dist:
            dist[nxt] = nxt_dist
            heapq.heappush(pq, (nxt_dist, nxt))
            
# 도착 못 하는 경우 -1
if dist[n-1] == INF:
    print(-1)
else:
    print(dist[n-1])