r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]
dir_list = [(-1,0), (1,0), (0, 1), (0, -1)]

def drowning(x, y):

    if maps[x][y] == '.':
        return False
    
    seas = 0
    for dx, dy in dir_list:

        nx, ny = x + dx, y + dy

        if not (0 <= nx < r and 0 <= ny < c):
            seas += 1

        elif maps[nx][ny] == '.':
            seas += 1

    return seas >= 3

future = [['.' for _ in range(c)] for _ in range(r)]

min_x, min_y = r-1, c-1
max_x, max_y = 0, 0
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'X' and not drowning(i, j):
            future[i][j] = 'X'
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)
            
for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        print(future[i][j], end='')
    print()