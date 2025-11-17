k = int(input())

dp = [[0] * 46 for _ in range(2)]

dp[0][0] = 1
dp[1][0] = 0

dp[0][1] = 0
dp[1][1] = 1

for i in range(2):

    for j in range(2, 46):

        dp[i][j] = dp[i][j-2] + dp[i][j-1]
        dp[i][j] = dp[i][j-2] + dp[i][j-1]

print(dp[0][k], dp[1][k])