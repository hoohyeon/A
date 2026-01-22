t = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

# union - rank
def union(a, b):
    ra = find(a)
    rb = find(b)

    # find 비교
    if ra == rb:
        return

    if rank[ra] < rank[rb]:
        parent[ra] = rb

    else:
        parent[rb] = ra

        # 같은 rank 합치면 rank += 1
        if rank[ra] == rank[rb]:
            rank[ra] += 1

# 두 영역이 통신 가능
def is_connected(a, b):
    x1, y1, r1 = circles[a]
    x2, y2, r2 = circles[b]

    dx = x1 - x2
    dy = y1 - y2

    return dx*dx + dy*dy <= (r1 + r2) * (r1 + r2)

for _ in range(t):
    n = int(input())
    circles = [tuple(map(int, input().split())) for _ in range(n)]

    parent = [i for i in range(n)]
    rank = [0] * n

    # 영역 개수 = n
    # union 마다 -1
    cnt = n
    for i in range(n-1):
        for j in range(i+1, n):
            if is_connected(i, j) and find(i) != find(j):
                union(i, j)
                cnt -= 1

    print(cnt)