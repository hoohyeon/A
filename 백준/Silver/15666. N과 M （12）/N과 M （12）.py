from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for cb in combinations_with_replacement(sorted(set(nums)), m):
    print(*cb)