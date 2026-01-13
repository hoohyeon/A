n, t = map(int, input().split())
time_score = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (t+1)
for k, s in time_score:
    # 0-1 Knapsack
    for i in range(t, k-1, -1):
        dp[i] = max(dp[i], dp[i-k] + s)

print(max(dp))