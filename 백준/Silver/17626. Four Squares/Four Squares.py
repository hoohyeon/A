import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

# 제곱수
j = 1
while j ** 2 <= n:
    dp[j**2] = 1
    j += 1

for i in range(1, n+1):
    if dp[i] == 0:
        j = 1
        while j ** 2 <= i:
            if dp[i] == 0:
                dp[i] = dp[j**2] + dp[i-(j**2)]
            else:
                dp[i] = min(dp[i], dp[j**2] + dp[i-(j**2)])
            j += 1
            
print(dp[n])