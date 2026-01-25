n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]

# 0-1 index
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = x[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

max_profit = -int(1e9)

# 한 변의 길이 : k
for k in range(1, n+1):
    for i in range(1, n-k+2):
        for j in range(1, n-k+2):
            
            # 시작점, 끝점
            x1, y1 = i, j
            x2, y2 = i + k - 1, j + k -1
            
            total = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
            
            max_profit = max(max_profit, total)
            
print(max_profit)