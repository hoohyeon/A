from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    def bfs(i, j):
        q = deque([(i, j)])
        visited[i][j] = True
        days = int(maps[i][j])
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                
                if visited[nr][nc]:
                    continue
                    
                if maps[nr][nc] == 'X':
                    continue                
                    
                days += int(maps[nr][nc])
                visited[nr][nc] = True
                q.append((nr, nc))
                
        return days
                
    answer = []
    
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and maps[r][c] != 'X':
                answer.append(bfs(r, c))
    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer