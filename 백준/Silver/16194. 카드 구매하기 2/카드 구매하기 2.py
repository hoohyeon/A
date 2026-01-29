n = int(input())
p = [0] + list(map(int, input().split()))

dp = [int(1e9)] * (n+1)
dp[0] = 0

# i장 뽑는 최소 값 = (i-j장을 뽑은 최솟값 + j장 뽑는 값) 중의 최솟값
# j : 1 ~ i
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + p[j])

print(dp[n])