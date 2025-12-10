from itertools import product

n, m = map(int, input().split())

l = [x for x in range(1, n+1)]

for p in product(l, repeat = m):
    print(*p)