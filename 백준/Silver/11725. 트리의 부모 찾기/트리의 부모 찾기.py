from collections import deque

n = int(input())

graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()

        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = node
                q.append(adj)

bfs(1)

for parent in visited[2:]:
    print(parent)