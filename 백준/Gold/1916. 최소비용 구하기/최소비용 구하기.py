import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
INF = 10**9
dist = [INF] * (n+1)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0
    
    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for next, w in graph[node]:
            cost = d + w

            if dist[next] > cost:
                dist[next] = cost

                heapq.heappush(pq, (cost, next))
                
s_city, e_city = map(int, input().split())

dijkstra(s_city)

print(dist[e_city])