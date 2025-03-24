from collections import deque
n, m = map(int, input().split())

move = {}

for _ in range(n + m):
    x, y = map(int, input().split())
    move[x] = y

queue = deque()
queue.append((1,0))

visited = [0] * 101

def bfs():
    while queue:
        now, cnt = queue.popleft()

        if now == 100:
            return cnt

        for i in range(1, 7):
            next = now + i
            if next > 100:
                continue

            if next in move:
                next = move[next]

            if not visited[next]:
                visited[next] = 1
                queue.append((next, cnt + 1))

print(bfs())