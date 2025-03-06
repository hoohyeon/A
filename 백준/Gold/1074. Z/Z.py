import sys
input = sys.stdin.readline

def find_z(N, x, y, order):
    if N == 0:
        print(order)
        return

    half = 2 ** (N-1)

    if r < x + half and c < y + half:   # 왼쪽 위
        find_z(N-1, x, y, order)

    elif r < x + half and c >= y + half: # 오른쪽 위
        find_z(N-1, x, y + half, order + half * half)

    elif r >= x + half and c < y + half: # 왼쪽 아래
        find_z(N-1, x + half, y, order + 2 * half * half)

    elif r >= x + half and c >= y + half: # 오른쪽 아래
        find_z(N-1, x + half, y + half, order + 3 * half * half)    

n, r, c = map(int, input().split())
find_z(n, 0, 0, 0)    # x, y = 0, 0 시작
