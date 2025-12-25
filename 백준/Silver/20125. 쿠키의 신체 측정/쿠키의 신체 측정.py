import sys
input = sys.stdin.readline

n = int(input())
cookie = [list(input()) for _ in range(n)]

# 머리, 심장 좌표 찾기
found = False
for row in range(n):
    for col in range(n):
        if cookie[row][col] == '*':
            head_row, head_col = row, col
            heart_row, heart_col = row + 1, col
            found = True
            break
        
    if found:
        break
    
# 왼팔
left_arm = 0
r, c = heart_row, heart_col - 1
while c >= 0 and cookie[r][c] == '*':
    left_arm += 1
    c -= 1
        
# 오른팔
right_arm = 0
r, c = heart_row, heart_col + 1
while c < n and cookie[r][c] == '*':
    right_arm += 1
    c += 1
        
# 허리
body = 0
r, c = heart_row + 1, heart_col
while r < n and cookie[r][c] == '*':
    body += 1
    r += 1

# 허리 끝 좌표
body_end_row, body_end_col = r-1, c

# 왼쪽 다리
left_leg = 0
r, c = body_end_row + 1, body_end_col - 1
while r < n and cookie[r][c] == '*':
    left_leg += 1
    r += 1
    
# 오른쪽 다리
right_leg = 0
r, c = body_end_row + 1, body_end_col + 1
while r < n and cookie[r][c] == '*':
    right_leg += 1
    r += 1
    
print(heart_row+1, heart_col+1)
print(left_arm, right_arm, body, left_leg, right_leg)