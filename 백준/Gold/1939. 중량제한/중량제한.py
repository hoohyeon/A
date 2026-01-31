import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    
    edges.append((c, a, b))

# 가중치 높은 순 정렬
edges.sort(reverse=True)

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

s, e = map(int, input().split())
max_w = 0

for w, a, b in edges:
    union(a, b)
    
    # 시작점과 끝점 연결
    # 현재 다리 중량이 최대 중량
    if find(s) == find(e):
        max_w = w
        break
    
print(max_w)