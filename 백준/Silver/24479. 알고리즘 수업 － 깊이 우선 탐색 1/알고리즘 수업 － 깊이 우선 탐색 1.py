import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호 오름차순 정렬
for i in range(1, n+1):
    graph[i].sort()

# 방문 순서 c
c = 1
def dfs(v):
    global c
    visit[v] = c

    for next in graph[v]:
        if not visit[next]:
            c += 1
            dfs(next)

dfs(r)

for v in visit[1:]:
    print(v)