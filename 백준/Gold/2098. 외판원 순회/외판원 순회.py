n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

# dp[cur][mask] = 현재 도시 : cur, 방문 도시 비트 : mask
dp = [[-1] * (1 << n) for _ in range(n)]
full = (1 << n) -1
INF = int(1e9)

def dfs(cur, mask):
    # 종료 조건
    if mask == full:
        if cost[cur][0] == 0:
            return INF
        
        return cost[cur][0]

    # 이미 계산한 값    
    if dp[cur][mask] != -1:
        return dp[cur][mask]
    
    dp[cur][mask] = INF
    
    # 다음 도시
    for nxt in range(n):
        # 이미 방문 도시 스킵
        if mask & (1 << nxt):
            continue
        
        # 갈 수 없는 도시 스킵
        if cost[cur][nxt] == 0:
            continue
        
        # 최소 비용 만드는 nxt
        dp[cur][mask] = min(dp[cur][mask], cost[cur][nxt] + dfs(nxt, mask | (1 << nxt)))
        
    return dp[cur][mask]

# 0번 도시 출발, 0번 도시만 방문
print(dfs(0, (1 << 0)))