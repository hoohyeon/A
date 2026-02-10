import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(node, cost):
    dist[node] = cost

    for next_node, weight in graph[node]:
        next_cost = cost + weight

        if dist[next_node] == -1:
            dfs(next_node, next_cost)

# 1st dfs
dist = [-1] * (n+1)
dfs(1, 0)

# 루트에서 가장 먼 점 = 지름 중 한 점
far_node = dist.index(max(dist))

# 2nd dfs
dist = [-1] * (n+1)
dfs(far_node, 0)

# 지름 중 한 점에서 가장 먼 점까지의 거리 = 트리의 지름
print(max(dist))