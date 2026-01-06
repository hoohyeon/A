import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

INF = int(1e9)
def dijkstra(s):
    # 이전 노드 배열
    prev = [-1] * (n+1)
    dist = [INF] * (n+1)
    dist[s] = 0
    
    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        cur_cost, cur = heapq.heappop(pq)

        if cur_cost > dist[cur]:
            continue
            
        for nxt, weight in graph[cur]:
            nxt_cost = cur_cost + weight

            if dist[nxt] > nxt_cost:
                dist[nxt] = nxt_cost
                prev[nxt] = cur
                heapq.heappush(pq, (nxt_cost, nxt))

    return dist, prev

dist, prev = dijkstra(start)

# 경로 배열
path = []
cur = end

# 이전 노드로 경로 만들기
while cur != -1:
    path.append(cur)
    cur = prev[cur]

path.reverse()

print(dist[end])
print(len(path))
print(*path)