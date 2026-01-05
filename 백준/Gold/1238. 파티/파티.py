import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())

# x에서 최소 - graph, x까지 최소 - rev_graph
graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    # + 역방향 간선 
    graph[a].append((b, t))
    rev_graph[b].append((a, t))
    
INF = int(1e9)
def dijkstra(start, g):
    dist = [INF] * (n+1)
    dist[start] = 0
    
    pq = []
    heapq.heappush(pq, (0, start))
        
    while pq:
        cur_cost, cur = heapq.heappop(pq)
        
        if cur_cost > dist[cur]:
            continue
        
        for next_node, weight in g[cur]:
            next_cost = cur_cost + weight
            
            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                
                heapq.heappush(pq, (next_cost, next_node))
                
    return dist

# go - X -> i , back - i -> X
go = dijkstra(x, graph)
back = dijkstra(x, rev_graph)

max_time = 0
for i in range(1, n+1):
    max_time = max(max_time, go[i] + back[i])
    
print(max_time)