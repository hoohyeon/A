n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)]

# dp[r][c][d] = (r, c) 까지 직전에 d 방향으로 내려왔을 때의 최소 연료 합
INF = int(1e9)
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]

# 첫번째 열
for c in range(m):
    for d in range(3):
        dp[0][c][d] = fuel[0][c]
        
for r in range(1, n):
    for c in range(m):
        # d = 0
        if c + 1 < m:
            dp[r][c][0] = min(dp[r-1][c+1][1], dp[r-1][c+1][2]) + fuel[r][c]    
        
        # d = 1
        dp[r][c][1] = min(dp[r-1][c][0], dp[r-1][c][2]) + fuel[r][c]
        
        # d = 2
        if c - 1 >= 0:
            dp[r][c][2] = min(dp[r-1][c-1][0], dp[r-1][c-1][1]) + fuel[r][c]

min_fuel = INF
for c in range(m):
    min_fuel = min(min_fuel, min(dp[n-1][c]))

print(min_fuel)