n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(n):
    w, v = items[i][0], items[i][1]
    
    for j in range(1, k+1):

        if w > j:
            dp[i+1][j] = dp[i][j]

        else:
            dp[i+1][j] = max(dp[i][j-w] + v, dp[i][j])

print(dp[n][k])