from itertools import combinations

n, m = map(int, input().split())

num_list = [i+1 for i in range(n)]

for c in combinations(num_list, m):
    print(*c)