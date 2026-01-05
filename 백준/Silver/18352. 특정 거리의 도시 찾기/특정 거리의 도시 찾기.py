import sys
input = sys.stdin.readline

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    dist = [-1] * (n+1)
    dist[start] = 0

    q = deque([start])

    while q:
        cur = q.popleft()

        if dist[cur] == k:
            continue
            
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    return dist

dist = bfs(x)

found = False
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        found = True

if not found:
    print(-1)