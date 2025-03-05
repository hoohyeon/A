n = int(input())

floors = [0] * (n+1)

for i in range(1, n+1):
    floors[i] = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = floors[1]

    elif i == 2:
        dp[i] = floors[1] + floors[2]

    else:
        dp[i] = max(dp[i-3] + floors[i-1] + floors[i], dp[i-2] + floors[i])

print(dp[-1])