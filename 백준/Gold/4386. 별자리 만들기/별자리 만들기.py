n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]

# 정점 i에서 정점 j까지 가중치 dist 간선: (dist, i, j)
edges = []
for i in range(n-1):
    for j in range(i+1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        edges.append((dist, i, j))

# 가중치로 정렬
edges.sort()

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

cnt = 0
cost = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        cost += c

    # MST = 간선 n-1개
    if cnt == n-1:
        break

# 소수점 둘째 자리까지
print(f"{cost:.2f}")