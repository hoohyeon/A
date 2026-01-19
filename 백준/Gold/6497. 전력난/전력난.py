import sys
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    
    # 종료 조건
    if m == 0 and n == 0:
        break
        
    # 가중치 정렬
    edges = [tuple(map(int, input().split())) for _ in range(n)]
    edges.sort(key=lambda x:x[2])

    parent = [i for i in range(m)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
    
        if ra != rb:
            parent[rb] = ra
    
    before, after = 0, 0
    for e in edges:
        x, y, z = e
        before += z

        # 선택한 간선
        if find(x) != find(y):
            union(x, y)
            after += z
    
    print(before - after)