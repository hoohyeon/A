from itertools import combinations_with_replacement

n, m = map(int, input().split())

num_list = [i+1 for i in range(n)]

for c in combinations_with_replacement(num_list, m):
    print(*c)