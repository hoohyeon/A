n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
color = [list(map(int, input().split())) for _ in range(n)]

dp = [[(0, 0) for _ in range(m)] for _ in range(n)]
dp[0][0] = board[0][0], board[0][0]

for i in range(n):
    for j in range(m):
        # (0, 0)
        if i == 0 and j == 0:
            continue

        # 후보값
        candidates = []

        # 위에서 오는 경우
        if i > 0:
            # 흰색
            if color[i][j] == 0:
                candidates.append(dp[i-1][j][0] + board[i][j])
                candidates.append(dp[i-1][j][1] + board[i][j])
            # 검은색
            else:
                candidates.append(-(dp[i-1][j][0] + board[i][j]))
                candidates.append(-(dp[i-1][j][1] + board[i][j]))
        
        # 왼쪽에서 오는 경우
        if j > 0:
            # 흰색
            if color[i][j] == 0:
                candidates.append(dp[i][j-1][0] + board[i][j])
                candidates.append(dp[i][j-1][1] + board[i][j])
            # 검은색
            else:
                candidates.append(-(dp[i][j-1][0] + board[i][j]))
                candidates.append(-(dp[i][j-1][1] + board[i][j]))
        
        
        # 위에서 오는 경우
        # if i > 0:
        #     for v in (dp[i-1][j][0], dp[i-1][j][1]):
        #         temp = v + board[i][j]

        #         # 검은색이면 반전
        #         if color[i][j] == 1:
        #             temp = -temp
                    
        #         candidates.append(temp)
            
        # 왼쪽에서 오는 경우
        # if j > 0:
        #     for v in (dp[i][j-1][0], dp[i][j-1][1]):
        #         temp = v + board[i][j]

        #         # 검은색이면 반전
        #         if color[i][j] == 1:
        #             temp = -temp
                    
        #         candidates.append(temp)

        dp[i][j] = (max(candidates), min(candidates))

print(max(dp[n-1][m-1]))