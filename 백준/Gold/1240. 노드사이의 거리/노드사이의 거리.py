n, m = map(int, input().split())

# 그래프 (인접 리스트)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# dfs - 현재노드, 누적거리
def dfs(cur, dist):
    if cur == end:
        return dist

    for nxt, w in graph[cur]:
        if not visit[nxt]:
            visit[nxt] = True
            res = dfs(nxt, dist + w)
          
            # 성공
            if res != -1:
                return res
    # 실패
    return -1

for _ in range(m):
    start, end = map(int, input().split())
    
    visit = [False] * (n+1)
    visit[start] = True

    print(dfs(start, 0))