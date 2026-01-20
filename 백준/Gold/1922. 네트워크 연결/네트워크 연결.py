import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra

cost = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        cost += c

print(cost)