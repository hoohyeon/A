N, M, K = map(int, input().split())

fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    board = [[[] for _ in range(N)] for _ in range(N)]
    
    for r, c, m, s, d in fireballs:        
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        
        board[nr][nc].append([m, s, d])

    new_fireballs = []
    
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) == 0:
                continue
            
            if len(board[i][j]) == 1:
                m, s, d = board[i][j][0]
                new_fireballs.append([i, j, m, s, d])
                
            else:
                total_m = 0
                total_s = 0
                odd = 0
                even = 0
                
                for m, s, d in board[i][j]:
                    total_m += m
                    total_s += s
                    if d % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                    
                new_m = total_m // 5
                # 질량이 0인 파이어볼 소멸
                if new_m == 0:
                    continue
                
                new_s = total_s // len(board[i][j])
                
                # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수
                if odd == 0 or even == 0:
                    dirs = [0, 2, 4, 6]
                else:
                    dirs = [1, 3, 5, 7]
                    
                for nd in dirs:
                    new_fireballs.append([i, j, new_m, new_s, nd])
                    
    fireballs = new_fireballs
    
answer = sum(m for r, c, m, s, d in fireballs)

print(answer)