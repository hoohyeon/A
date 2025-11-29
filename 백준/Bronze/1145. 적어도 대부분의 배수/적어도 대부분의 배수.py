from itertools import combinations
import math

n = list(map(int, input().split()))

m = int(1e9)
for c in combinations(n, 3):
    l = math.lcm(*c)
    
    m = min(m, l)
    
print(m)    