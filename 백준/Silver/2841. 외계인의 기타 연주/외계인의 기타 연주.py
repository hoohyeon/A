import sys
input = sys.stdin.readline

n, p = map(int, input().split())
guitar = [[] for _ in range(7)]

cnt = 0
for _ in range(n):
    line, fret = map(int, input().split())
    
    # 손 떼기
    while guitar[line] and guitar[line][-1] > fret:
            guitar[line].pop()
            cnt += 1
    
    # 프렛 누르기
    if not guitar[line] or guitar[line][-1] < fret:
        guitar[line].append(fret)
        cnt += 1

print(cnt)