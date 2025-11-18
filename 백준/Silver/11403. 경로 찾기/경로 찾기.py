from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * n for _ in range(n)]

for s in range(n):
    q = deque([s])
    visit = [False] * n

    while q:
        c = q.popleft()

        for next in range(n):
            if g[c][next] == 1 and not visit[next]:
                visit[next] = True
                q.append(next)
                result[s][next] = 1
            
for row in result:
    print(*row)