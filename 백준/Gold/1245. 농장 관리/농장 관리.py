n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
cnt = 0

def dfs(r, c):
    height = grid[r][c]
    stack = [(r, c)]
    visited[r][c] = True
    is_peak = True
    
    while stack:
        r, c = stack.pop()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if grid[nr][nc] > height:
                is_peak = False

            elif not visited[nr][nc] and grid[nr][nc] == height:
                stack.append((nr, nc))
                visited[nr][nc] = True

    return is_peak

for i in range(n):
    for j in range(m):
        if not visited[i][j] and dfs(i, j):
            cnt += 1

print(cnt)