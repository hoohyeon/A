from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    visit = [False] * 10000
    
    q = deque([(a, "")])
    visit[a] = True
  
    while q:
        num, path = q.popleft()

        if num == b:
            print(path)
            break

        # D
        d = (num * 2) % 10000
        if not visit[d]:
            q.append((d, path + 'D'))
            visit[d] = True
            
        # S
        s = (num - 1) % 10000
        if not visit[s]:
            q.append((s, path + 'S'))
            visit[s] = True
            
        # L
        l = (num % 1000) * 10 + (num // 1000)
        if not visit[l]:
            q.append((l, path + 'L'))
            visit[l] = True

        # R
        r = (num % 10) * 1000 + (num // 10)
        if not visit[r]:
            q.append((r, path + 'R'))
            visit[r] = True