n = int(input())
card = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    best = 0    
    
    for j in range(1, i+1):
        best = max(best, dp[i-j] + card[j-1])

    dp[i] = best
    
print(dp[n])