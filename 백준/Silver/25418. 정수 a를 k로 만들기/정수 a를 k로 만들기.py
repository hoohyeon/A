from collections import deque

a, k = map(int, input().split())

q = deque([(a, 0)])

visit = [False] * (k + 1)
visit[a] = True

while q:
    now, cnt = q.popleft()

    if now == k:
        break

    if now + 1 <= k and not visit[now+1]:
        visit[now+1] = True
        q.append((now+1, cnt+1))
    
    if now * 2 <= k and not visit[now*2]:
        visit[now*2] = True
        q.append((now*2, cnt+1))

print(cnt)