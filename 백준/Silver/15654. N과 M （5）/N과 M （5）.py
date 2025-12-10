from itertools import permutations

n, m = map(int, input().split())
l = list(map(int, input().split()))

for c in permutations(sorted(l), m):
    print(*c)