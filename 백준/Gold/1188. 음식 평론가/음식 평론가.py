import math

n, m = map(int, input().split())

g = math.gcd(n, m)

# m-1 : 조각 m개 만들기 위해 m-1 번 칼질
# g-1 : 최대공약수 g개씩 묶어 g-1 번 칼질 감소
# r : 최소 칼질 횟수
r = (m - 1) - (g- 1)

print(r)