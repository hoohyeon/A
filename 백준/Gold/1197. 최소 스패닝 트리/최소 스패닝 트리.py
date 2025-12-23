import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

# 가중치로 정렬 
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra 

cost, cnt = 0, 0
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        cost += w
        cnt += 1
        
        # MST의 간선 개수 = V-1
        if cnt == V-1:
            break

print(cost)