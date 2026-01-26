import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, t, m = map(int, input().split())

    teams = {}
    for time in range(m):
        i, j, s = map(int, input().split())

        if i not in teams:
            teams[i] = {
                "scores" : [0] * (k+1),
                "submit" : 0,
                "last" : 0
            }

        teams[i]["scores"][j] = max(teams[i]["scores"][j], s)
        teams[i]["submit"] += 1
        teams[i]["last"] = time
    
    ranking = []
    for team_id in teams:
        total = sum(teams[team_id]["scores"])
        submit = teams[team_id]["submit"]
        last = teams[team_id]["last"]

        ranking.append((team_id, total, submit, last))

    # 최종 점수 높은 순, 제출 횟수 적은 순, 제출 시간 빠른 순
    ranking.sort(key=lambda x:(-x[1], x[2], x[3]))

    # 팀의 순위
    rank = 0
    for idx, team in enumerate(ranking):
        if team[0] == t:
            rank = idx + 1
            break

    print(rank)