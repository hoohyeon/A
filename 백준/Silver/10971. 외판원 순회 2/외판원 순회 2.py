n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_cost = int(1e9)

def dfs(start, now, depth, cost):
    global min_cost

    # 가지치기
    if cost >= min_cost:
        return

    # 방문 완료
    if depth == n:
        if w[now][start] != 0:
            min_cost = min(cost + w[now][start], min_cost)
        return

    for next in range(n):
        if not visited[next] and w[now][next] != 0:
            visited[next] = True
            dfs(start, next, depth + 1, cost + w[now][next])
            visited[next] = False

visited[0] = True
dfs(0, 0, 1, 0)
print(min_cost)