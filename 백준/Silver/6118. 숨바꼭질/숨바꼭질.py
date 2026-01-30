from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n+1)
dist[1] = 0

q = deque([(1, 0)])

while q:
    cur, cur_cost = q.popleft()

    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = cur_cost + 1
            q.append((nxt, cur_cost + 1))

max_dist = max(dist)
num = dist.index(max_dist)
cnt = dist.count(max_dist)

print(num, max_dist, cnt)