n = int(input())

t = []
p = []

dp = [0] * (n+2)

for _ in range(n):
    ti, pi = map(int, input().split())

    t.append(ti)
    p.append(pi)

for i in range(n):

    dp[i+1] = max(dp[i+1], dp[i])

    if i + t[i] <= n:
        dp[i+t[i]] = max(dp[i+t[i]], dp[i] + p[i])

print(max(dp))