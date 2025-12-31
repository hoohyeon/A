k = int(input())

dirs, lens = [], []
max_width, max_height = 0, 0

for _ in range(6):
    d, l = map(int, input().split())
    dirs.append(d)
    lens.append(l)

# 최대 가로, 세로 인덱스 (배열에서의 위치)
w_idx, h_idx = -1, -1

for i in range(6):
    # 가로
    if dirs[i] in (1, 2):
        if max_width < lens[i]:
            max_width = lens[i]
            w_idx = i
    
    # 세로
    if dirs[i] in (3, 4):
        if max_height < lens[i]:
            max_height = lens[i]
            h_idx = i

# 작은 사각형의 가로, 세로 인덱스
# 최대 인덱스의 양 옆 값의 차이
small_width = abs(lens[(h_idx-1) % 6] - lens[(h_idx+1) % 6])
small_height = abs(lens[(w_idx-1) % 6] - lens[(w_idx+1) % 6])

# 참외 개수
cnt = k * (max_width * max_height - small_width * small_height)

print(cnt)