import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
buttons = list(map(int, input().split()))

# +, - 로만 이동
min_cnt = abs(n-100)

for channel in range(1000000):
    str_channel = str(channel)
    
    # 고장난 버튼 있으면 이동 X
    for c in str_channel:
        if int(c) in buttons:
            break

    # 고장난 버튼 없으면
    else:
        min_cnt = min(min_cnt, len(str_channel) + abs(channel - n))

print(min_cnt)            