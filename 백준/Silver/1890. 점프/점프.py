n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for row in range(n):
    for col in range(n):
        
        if dp[row][col] == 0:
            continue

        if row == n-1 and col == n-1:
            continue        
        
        k = grid[row][col]

        if row + k < n:
            dp[row+k][col] += dp[row][col]

        if col + k < n:
            dp[row][col+k] += dp[row][col]

print(dp[n-1][n-1])