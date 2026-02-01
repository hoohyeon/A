s = input()
n = int(input())

# 반지 이어붙이기
rings = [input() * 2 for _ in range(n)]

cnt = 0
for r in rings:
    if s in r:
        cnt += 1
        
print(cnt)