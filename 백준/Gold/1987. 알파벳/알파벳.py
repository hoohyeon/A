r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

# visit[0] = 'A' 방문
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visit = [False] * 26
max_cnt = 0

def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < r and 0 <= ny < c:
            idx = ord(board[nx][ny]) - 65

            if not visit[idx]:
                visit[idx] = True
                dfs(nx, ny, cnt + 1)
                visit[idx] = False
                
visit[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)
print(max_cnt)