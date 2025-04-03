from collections import deque

a, b = map(int, input().split())

queue = deque()
queue.append((a, 1))

def bfs():
    while queue:
        cur, cnt = queue.popleft()

        if cur > b:
            continue
        
        if cur == b:
            return cnt

        queue.append((cur * 2, cnt + 1))
        queue.append((int(str(cur)+'1'), cnt + 1))

    return -1

print(bfs())