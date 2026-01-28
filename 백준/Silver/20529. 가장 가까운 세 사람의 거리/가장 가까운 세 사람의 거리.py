from collections import Counter
from itertools import combinations

t = int(input())

for _ in range(t):
    n = int(input())
    mbti = input().split()
    
    # 최대 심리적 거리
    dist = 12
    
    cnt = Counter(mbti)
    
    # 같은 mbti 3명 이상 : 무조건 0
    if max(cnt.values()) >= 3:
        dist = 0

    # 그렇지 않은 경우 브루트포스
    else:
        for a, b, c in combinations(mbti, 3):
            d = 0

            for i in range(4):
                if a[i] != b[i]:
                    d += 1
                if b[i] != c[i]:
                    d += 1
                if c[i] != a[i]:
                    d += 1

            dist = min(dist, d)

    print(dist)