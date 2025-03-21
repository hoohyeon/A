n = int(input())

numbers = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = numbers[i]

    dp[i] = max(dp[i-1] + numbers[i], numbers[i])

print(max(dp))