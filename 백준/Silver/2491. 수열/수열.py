n = int(input())
l = list(map(int, input().split()))

dp = [[1] * n for _ in range(2)]

for i in range(1, n):
    if l[i] >= l[i-1]:
        dp[0][i] = dp[0][i-1] + 1
    
    if l[i] <= l[i-1]:
        dp[1][i] = dp[1][i-1] + 1
        
print(max(max(dp[0]), max(dp[1])))