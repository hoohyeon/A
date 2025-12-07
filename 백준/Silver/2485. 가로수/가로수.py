import math

n = int(input())
tree = [int(input()) for _ in range(n)]

gap = [tree[i+1] - tree[i] for i in range(n-1)]

g = gap[0]
for d in gap[1:]:
    g = math.gcd(g, d)
    
d = sum((gap[i] // g) - 1 for i in range(n-1))
print(d)