n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
m = [0] * n

for i in range(n):
    mate = 0
    for j in range(n):
        if i == j:
            continue
        
        for k in range(5):
            if c[i][k] == c[j][k]:
                mate += 1
                break

    m[i] = mate

print(m.index(max(m)) + 1)