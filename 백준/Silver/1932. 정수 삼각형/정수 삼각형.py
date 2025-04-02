n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * i for i in range(1, n+1)]
dp[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            prev = dp[i-1][0]

        elif j == i:
            prev = dp[i-1][j-1]

        else:
            prev = max(dp[i-1][j-1], dp[i-1][j])

        dp[i][j] = prev + tri[i][j]

print(max(dp[n-1]))