import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    
    if ra != rb:
        parent[rb] = ra      

# 초기값 0
cycle_turn = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    
    # 사이클 
    if find(a) == find(b):
        cycle_turn = i
        break
        
    else:
        union(a, b)
        
print(cycle_turn)