n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

# dp[x][y] = (x, y)를 오른쪽 아래로 하는 최대 정사각형 한 변 길이
dp = [[0] * m for _ in range(n)]

max_size = 0
for i in range(n):
    for j in range(m):
        # 현재 칸 = 0
        if board[i][j] == 0:
            dp[i][j] = 0

        # 현재 칸 = 1
        else:
            # 1열 or 1행 (왼쪽, 위 존재 X)
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        # 최대 길이 갱신
        max_size = max(max_size, dp[i][j])

print(max_size ** 2)