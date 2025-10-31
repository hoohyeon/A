n = int(input())

inf = int(10e9)

dp = [inf] * (100000 + 1)

dp[2], dp[4], dp[5] = 1, 2, 1

for i in range(6, 100000 + 1):
    dp[i] = min(dp[i-2] + 1, dp[i-5] + 1)
    
if dp[n] == inf:
    print(-1)
else:
    print(dp[n])