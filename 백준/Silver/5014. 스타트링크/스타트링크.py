from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [-1] * (f+1)

q = deque([s])
visited[s] = 0
result = -1

while q:
    now = q.popleft()

    if now == g:
        result = visited[g]
        break
        
    for next in (now+u, now-d):
        if not 1 <= next <= f:
            continue

        if not visited[next] == -1:
            continue
            
        visited[next] = visited[now] + 1

        q.append(next)

print('use the stairs' if result == -1 else result)