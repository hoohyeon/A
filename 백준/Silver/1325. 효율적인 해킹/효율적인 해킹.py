from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]
 
for _ in range(m):
    a, b = map(int, input().split())

    adj[b].append(a)

def bfs(start):
    q = deque([(start)])
    visit = [False] * (n+1)
    visit[start] = True
    cnt = 1
    
    while q:
        cur = q.popleft()

        for next in adj[cur]:
            if visit[next]:
                continue

            visit[next] = True
            cnt += 1
            q.append(next)

    return cnt

cnt_list = [0] + [bfs(i) for i in range(1, n+1)]

max_cnt = max(cnt_list)

for i in range(1, n+1):
    if cnt_list[i] == max_cnt:
         print(i, end=' ')