n, d = map(int, input().split())
shortcut = [list(map(int, input().split())) for _ in range(n)]

dp = [i for i in range(d+1)]
    
for i in range(d+1):
    # 1
    dp[i] = min(dp[i], dp[i-1] + 1)
    
    # 2
    for s, e, l in shortcut:
        if i == s and e <= d:
            dp[e] = min(dp[e], dp[s] + l)
            
print(dp[d])