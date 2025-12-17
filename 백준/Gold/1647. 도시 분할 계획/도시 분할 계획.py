import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 비용 기준 정렬
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

# 자기 자신이 루트
parent = [i for i in range(n+1)]

# 루트 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 간선 연결
def union(x, y):
    rx = find(x)
    ry = find(y)

    # 이미 연결되어 있으면 선택 X
    if rx == ry:
        return False

    # x-y 간선 선택
    parent[ry] = rx
    return True

total = 0
max_cost = 0
for cost, start, end in edges:
    if union(start, end):
        total += cost
        max_cost = max(max_cost, cost)

print(total - max_cost)