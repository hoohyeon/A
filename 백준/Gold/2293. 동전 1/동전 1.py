n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for c in coins:
    for money in range(c, k+1):        
        dp[money] += dp[money-c]
        
print(dp[k])