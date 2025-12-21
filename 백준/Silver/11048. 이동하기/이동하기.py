n, m = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = max(dp[i][j+1] + candy[i][j], # 위쪽에서 오기
                           dp[i+1][j] + candy[i][j]) # 왼쪽에서 오기

print(dp[n][m])