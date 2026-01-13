n, m = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

max_cost = sum(C)
dp = [0] * (max_cost + 1)

for i in range(n):
    memory = A[i]
    cost = C[i]

    for j in range(max_cost, cost-1, -1):
        dp[j] = max(dp[j], dp[j-cost] + memory)

for c in range(max_cost+1):
    if dp[c] >= m:
        print(c)
        break