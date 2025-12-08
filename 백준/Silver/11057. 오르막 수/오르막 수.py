n = int(input())

# dp[i][j] = 길이가 i, 끝이 j
dp = [[0] * 10 for _ in range(1001)]

for row in range(1, 1001):
    for col in range(10):

        if row == 1:
            dp[row][col] = 1

        elif row == 2:
            dp[row][col] = col + 1

        else:
            for k in range(col+1):
                dp[row][col] += (dp[row-1][k] % 10007)

print(sum(dp[n]) % 10007)