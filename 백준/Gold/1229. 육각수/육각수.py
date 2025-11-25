import sys
input = sys.stdin.readline

n = int(input())
hex = []
dp = [7] * (n+1)

k = 1
while True:
    h = (2*k-1) * k

    if h > n:
        break

    hex.append(h)
    k += 1

dp[0] = 0
for h in hex:
    for i in range(h, n+1):
        dp[i] = min(dp[i], dp[i-h] + 1)

print(dp[n])