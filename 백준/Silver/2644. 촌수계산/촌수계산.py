from collections import deque

n = int(input())
s, e = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

q = deque([(s)])
dist = [-1] * (n+1)
dist[s] = 0

while q:
    cur = q.popleft()

    if cur == e:
        break

    for next in adj[cur]:
        if dist[next] == -1:
            dist[next] = dist[cur] + 1
            q.append(next)

print(dist[e])