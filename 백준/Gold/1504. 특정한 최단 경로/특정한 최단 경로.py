import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    # start 노드 기준 최소 거리 배열
    dist = [INF] * (n+1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        # 더 짧은 경로가 있으면 continue
        if cur_dist > dist[cur_node]:
            continue

        # 현재 노드와 인접한 노드들 검사
        for next_node, cost in graph[cur_node]:
            next_dist = cur_dist + cost
            if dist[next_node] > next_dist:
                dist[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))
    
    return dist

dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# 1 -> v1 -> v2 -> n
path1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
# 1 -> v2 -> v1 -> n
path2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]

answer = min(path1, path2)

if answer < INF:
    print(answer)
else:
    print(-1)