R, C, K = map(int, input().split())
maps = [list(input()) for _ in range(R)]

visit = [[False] * C for _ in range(R)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(r, c, d):
    # 거리 K
    if d == K:
        # 도착 = 집
        if (r, c) == (0, C-1):
            return 1
        return 0
        
    cnt = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if not (0 <= nr < R and 0 <= nc < C):
            continue

        if maps[nr][nc] == 'T':
            continue

        if visit[nr][nc]:
            continue

        visit[nr][nc] = True
        cnt += dfs(nr, nc, d+1)
        visit[nr][nc] = False
      
    return cnt

# 시작점 방문 처리
visit[R-1][0] = True

# (R-1, 0)에서 거리 1로 시작
print(dfs(R-1, 0, 1))