from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

# 집, 치킨집
homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# 치킨집 중 m개
for comb in combinations(chickens, m):
    city_dist = 0
    for hr, hc in homes:
        dist = float('inf')
        for cr, cc in comb:
            dist = min(dist, abs(hr-cr) + abs(hc-cc))
        city_dist += dist
    answer = min(answer, city_dist)
  
print(answer)