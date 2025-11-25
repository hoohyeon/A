import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    v = list(tuple(map(int, input().split())) for _ in range(n))

    s = sorted(v, key= lambda x:x[0])

    cnt, rank = 1, s[0][1]
    
    for i in range(1, n):
        next_rank = s[i][1]

        if rank > next_rank:
            cnt += 1
            rank = next_rank
            
    print(cnt)