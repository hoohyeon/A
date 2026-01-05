import sys, heapq
input = sys.stdin.readline

n, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = int(1e9)
def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur = heapq.heappop(pq)

        # 이미 더 가까운 경로
        if cur_cost > dist[cur]:
            continue

        for next_node, weight in graph[cur]:
            next_cost = cur_cost + weight

            # next_node 사용
            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))

    return dist

# k를 시작점으로 하는 거리 배열
dist = dijkstra(k)

for d in dist[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)