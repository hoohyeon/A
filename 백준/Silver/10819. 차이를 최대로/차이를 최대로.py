from itertools import permutations

n = int(input())
A = list(map(int, input().split()))

max_s = 0
for p in permutations(A, n):
    p = list(p)
    s = 0
    
    for i in range(1, n):
        s += abs(p[i] - p[i-1])
    
    max_s = max(max_s, s)

print(max_s)