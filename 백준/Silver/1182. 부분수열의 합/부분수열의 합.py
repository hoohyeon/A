from itertools import combinations

N, S = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    # i개 조합
    for c in combinations(A, i):
        if sum(c) == S:
            cnt += 1

print(cnt)