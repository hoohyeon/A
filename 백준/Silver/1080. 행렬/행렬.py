n, m = map(int, input().split())

a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]

cnt = 0

def flip(x, y):
    for i in range(3):
        for j in range(3):
            a[x+i][y+j] ^= 1

for r in range(n-2):

    for c in range(m-2):

        if a[r][c] != b[r][c]:

            flip(r, c)

            cnt += 1
    
if a == b:
    print(cnt)

else:
    print(-1)