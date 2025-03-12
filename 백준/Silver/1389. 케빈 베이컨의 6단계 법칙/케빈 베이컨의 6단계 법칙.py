import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque([start])
    
    visited  = [-1] * (n+1)
    visited [start] = 0

    while queue:

        node = queue.popleft()

        for neighbor in graph[node]:
            if visited [neighbor] == -1:
                visited [neighbor] = visited [node] + 1
                queue.append(neighbor)

    return visited 

min = float('inf')
ans = 0

for i in range(1, n+1):
    kevin_bacon = sum(bfs(i)[1:])

    if min > kevin_bacon:
        min = kevin_bacon
        ans = i

print(ans)