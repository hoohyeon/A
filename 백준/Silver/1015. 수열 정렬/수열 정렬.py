n = int(input())

arr = list(map(int, input().split()))

indexed = sorted([(val, idx) for idx, val in enumerate(arr)])

p = [0] * n

for new_idx, (_, original_idx) in enumerate(indexed):
    p[original_idx] = new_idx
    
print(*p)