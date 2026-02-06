n = int(input())
x = [tuple(map(int, input().split())) for _ in range(n)]

d = [b - a for a, b in x]
d.sort()

# n 홀수 : 중앙값 -> 1 
if n % 2 == 1:
    t = 1

# n 짝수 : 중앙값 사이 구간 전체
else:
    t = d[n//2] - d[n//2 - 1] + 1

print(t)