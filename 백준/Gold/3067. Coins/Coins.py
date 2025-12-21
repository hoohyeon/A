t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    # dp[x] = x원 경우의 
    dp = [0] * (m+1)
    dp[0] = 1
    
    for c in coins:
        for money in range(c, m+1):
            # c원 동전 사용
            dp[money] += dp[money-c]
            
    print(dp[m])