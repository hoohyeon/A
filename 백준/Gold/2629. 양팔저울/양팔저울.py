n = int(input())
W = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

# 가능한 무게 - 0으로 시작
possible = {0}

# 각 추에 대해
for w in W:
    # 다음 가능한 무게
    next_possible = set()

    for x in possible:
        next_possible.add(x)
        next_possible.add(x + w)
        next_possible.add(abs(x - w))

    possible = next_possible

for bead in M:
    if bead in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')