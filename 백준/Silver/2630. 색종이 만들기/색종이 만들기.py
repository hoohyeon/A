n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# 현재 영역 같은 색 확인
def color(n, x, y):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                return False
    return True

# 색종이 카운트
def count_papers(n, x, y):
    if color(n, x, y):
        if paper[x][y] == 0:
            return (1, 0)
        else:
            return (0, 1)

    half = n // 2

    w1, b1 = count_papers(half, x, y)
    w2, b2 = count_papers(half, x, y + half)
    w3, b3 = count_papers(half, x + half, y)
    w4, b4 = count_papers(half, x + half, y + half)

    return (w1+w2+w3+w4, b1+b2+b3+b4)

# n = n, x = 0, y = 0 시작
w, b = count_papers(n, 0, 0)

print(w)
print(b)