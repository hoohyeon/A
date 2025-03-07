import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        dp[1] = 1
    
    elif i == 2:
        dp[2] = 3

    else:
        dp[i] = 2 * dp[i-2] + dp[i-1]

print(dp[-1] % 10007)