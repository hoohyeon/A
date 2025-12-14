n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

# dp[i][r][c] = i번째 모양(0 가로, 1 세로, 2 대각선)으로 끝을 grid[r][c]에 놓을 수 있는 파이프 개수
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2, n):
    # 초기 가로 파이프
    if grid[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for r in range(1, n):
    for c in range(1, n):
        # 가로, 세로
        if grid[r][c] == 0:
            dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]

        # 대각선
        if grid[r][c] == 0 and grid[r-1][c] == 0 and grid[r][c-1] == 0:
            dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

print(sum(dp[i][n-1][n-1] for i in range(3)))