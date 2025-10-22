import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start, graph):
    distance = [INF] * len(graph)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distance[current_node]:
            continue

        for neighbor, edge_cost in graph[current_node]:
            new_dist = current_dist + edge_cost
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distance

n = int(input())
a, b, c = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    d, e, l = map(int, input().split())
    graph[d].append((e, l))
    graph[e].append((d, l))

distA = dijkstra(a, graph)
distB = dijkstra(b, graph)
distC = dijkstra(c, graph)

max_value = 0
max_node = 0
for i in range(1, n+1):
    value = min(distA[i], distB[i], distC[i])
    if value > max_value:
        max_value = value
        max_node = i
    elif value == max_value:
        max_node = min(max_node, i)

print(max_node)