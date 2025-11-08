from collections import deque

n, m = map(int, input().split())
index_list = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

cnt = 0
for idx in index_list:
    while True:
        if dq[0] == idx:
            dq.popleft()
            break
        else:
            if dq.index(idx) <= len(dq) // 2:
                dq.rotate(-1)
            else:
                dq.rotate(1)

            cnt += 1
            
print(cnt)