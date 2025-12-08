import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
k = int(input())

graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, cost in graph[now]:
            if dist + cost < distance[next]:
                distance[next] = dist + cost
                heapq.heappush(q, (dist + cost, next))

dijkstra(k)

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)