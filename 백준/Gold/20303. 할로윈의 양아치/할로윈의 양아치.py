n, m, k = map(int, input().split())
c = list(map(int, input().split()))
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

for _ in range(m):
    a, b = map(int, input().split())

    union(a, b)

group = {}
for i in range(1, n+1):

    r = find(i)

    # 새로운 root = 새로운 group
    # group[root] : [인원 수, 사탕 수]
    if r not in group:
        group[r] = [0, 0]

    # 인원 수 += 1, 사탕 수 += c[i-1]
    group[r][0] += 1
    group[r][1] += c[i-1]

# [인원 수, 사탕 수]
friend_candy = list(group.values())

# dp[i] = i명을 데려갔을 때 얻을 수 있는 최대 사탕 수
# 최대 k-1명
dp = [0] * k

# 0/1 Knapsack
for f, c in friend_candy:
    for i in range(k-1, f-1, -1):
        dp[i] = max(dp[i], dp[i-f] + c)

print(max(dp))