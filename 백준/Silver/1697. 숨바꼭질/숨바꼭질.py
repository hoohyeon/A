import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, k):
    queue = deque()
    queue.append((n, 0))

    visited = [0] * 100001
    visited[n] = 1

    while queue:
        x, time = queue.popleft()

        if x == k:
            return time

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and visited[nx] == 0:
                queue.append((nx, time+1))
                visited[nx] = 1
        

n , k = map(int, input().split())
print(bfs(n, k))