n, m = map(int, input().split())

grid = [list(map(int, input())) for _ in range(n)]

# 사각형, 변의 길이
def vertex(rectangle, x):
    for i in range(n - x + 1):
        for j in range(m - x + 1):
            if rectangle[i][j] == rectangle[i][j+x-1] == rectangle[i+x-1][j] == rectangle[i+x-1][j+x-1]:
                return True
    return False

max_side = 1
max_len = min(n, m)
for side in range(2, max_len+1):
    if vertex(grid, side):
        max_side = max(max_side, side)

print(max_side ** 2)