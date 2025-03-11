import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

# graph
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# bfs
def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)

# count
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)