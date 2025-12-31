from collections import deque

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]
board[0][0] = 2

# 사과
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

d = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]    

# 방향 전환 딕셔너리
turn = {}
L = int(input())
for _ in range(L):
    X, C = input().split()
    turn[int(X)] = C

snake = deque([(0, 0)])
time = 0

while True:
    time += 1
    
    # 현재 머리
    r, c = snake[0] 
    nr, nc = r + dr[d], c + dc[d]
    
    # 벽
    if not (0 <= nr < n and 0 <= nc < n):
        break
    
    # 자기 몸
    if board[nr][nc] == 2:
        break
    
    # 머리 이동
    snake.appendleft((nr, nc))
    
    # 다음 칸에 사과 O 
    if board[nr][nc] == 1:
        board[nr][nc] = 2
    
    # 다음 칸에 사과 X
    else:
        board[nr][nc] = 2
        tr, tc = snake.pop()
        board[tr][tc] = 0
        
    if time in turn:
        if turn[time] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
            
print(time)