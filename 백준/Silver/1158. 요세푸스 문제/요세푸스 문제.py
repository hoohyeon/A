from collections import deque

n, k = map(int, input().split())

q = deque(range(1, n+1))

l = list(range(1, n+1))

result = []

# while q:
#     q.rotate(-k)
#     result.append(q.pop())

idx = 0
while l:
    idx = (idx + k - 1) % len(l) 
    result.append(l.pop(idx))

print('<' + ", ".join(map(str, result)) + ">")