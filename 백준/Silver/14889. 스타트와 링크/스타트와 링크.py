import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
people = list(range(N))
half = N // 2

# 팀 능력치 계산
def team_stat(team):
    stat = 0
    
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a, b = team[i], team[j]
            stat += (S[a][b] + S[b][a])
    
    return stat

# 팀 조합에 따른 최소 능력치 합 차이
min_gap = int(1e9)   
for team_start in combinations(people, half):
    team_link = [x for x in people if x not in team_start]

    start_score = team_stat(team_start)
    link_score = team_stat(team_link)

    min_gap = min(min_gap, abs(start_score - link_score))

print(min_gap)