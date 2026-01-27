import sys
input = sys.stdin.readline

n = int(input())
broken = [False] * int(1e6 + 1)

cnt = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    
    # 안 깨져있으면 새로 부수기
    if not (broken[a] or broken[b] or broken[c]):
        cnt += 1
        
    broken[a] = True
    broken[b] = True
    broken[c] = True
    
print(cnt)