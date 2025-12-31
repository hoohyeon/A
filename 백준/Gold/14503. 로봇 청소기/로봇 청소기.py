n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 청소한 칸
cleaned = 0

while True:
    # 청소하지 않은 칸
    if room[r][c] == 0:
        room[r][c] = 2
        cleaned += 1
    
    # 주변에 청소 안 된 칸 있는지
    found = False
    
    for _ in range(4):
        # 왼쪽으로 회전
        d = (d-1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        
        # 청소하지 않은 빈 칸
        if room[nr][nc] == 0:
            r, c = nr, nc
            found = True
            break
    
    # 네 방향 모두 청소 or 벽
    if not found:
        # 후진 방향 (그대로 후진이라 d는 유지)
        back_d = (d-2) % 4
        
        br = r + dr[back_d]
        bc = c + dc[back_d]
        
        # 뒤가 벽이라면 종료
        if room[br][bc] == 1:
            break
        
        # 청소하지 않은 빈 칸 (이동 가능)
        else:
            r, c = br, bc
            
print(cleaned)