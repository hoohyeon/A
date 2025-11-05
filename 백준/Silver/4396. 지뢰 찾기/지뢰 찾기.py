def find_bomb(grid, x, y, n):
    cnt = 0
    for nx in range(-1, 2):
        for ny in range(-1, 2):
            if nx == ny == 0:
                continue
            
            if (0 <= x+nx < n) and (0 <= y+ny < n):
            
                if grid[x+nx][y+ny] == '*':
                    cnt += 1
    return cnt

def game_over():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                result_grid[i][j] = '*'

n = int(input())

grid = [list(input()) for _ in range(n)]
game_grid = [list(input()) for _ in range(n)]
result_grid = [['.' for _ in range(n)] for _ in range(n)]

exploded = False
for i in range(n):
    for j in range(n):

        if game_grid[i][j] == 'x':
            
            if grid[i][j] == '*':
                exploded = True
            else:
                result_grid[i][j] = str(find_bomb(grid, i, j, n))            
            
if exploded:
    game_over()

for line in result_grid:
    print(''.join(line))