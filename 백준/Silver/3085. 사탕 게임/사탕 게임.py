n = int(input())
c = [list(input()) for _ in range(n)]

def check_row(x):
    max_streak, streak = 1, 1
    for col in range(1, n):
        if c[x][col] == c[x][col-1]:
            streak += 1
            
        else:
            streak = 1
        max_streak = max(max_streak, streak)
    return max_streak

def check_col(y):
    max_streak, streak = 1, 1
    for row in range(1, n):
        if c[row][y] == c[row-1][y]:
            streak += 1
            
        else:
            streak = 1
        max_streak = max(max_streak, streak)

    return max_streak

# 초기 최대 개수
candy = 1
for i in range(n):
    candy = max(candy, check_row(i), check_col(i))

# 오른쪽 교환
for i in range(n):
    for j in range(n-1):
        if c[i][j] == c[i][j+1]:
            continue

        c[i][j], c[i][j+1] = c[i][j+1], c[i][j]
        candy = max(candy, check_row(i), check_col(j), check_col(j+1))
        c[i][j], c[i][j+1] = c[i][j+1], c[i][j]        
        
# 아래쪽 교환
for i in range(n-1):
    for j in range(n):
        if c[i][j] == c[i+1][j]:
            continue

        c[i][j], c[i+1][j] = c[i+1][j], c[i][j]
        candy = max(candy, check_row(i), check_row(i+1), check_col(j))
        c[i][j], c[i+1][j] = c[i+1][j], c[i][j]        
        
print(candy)