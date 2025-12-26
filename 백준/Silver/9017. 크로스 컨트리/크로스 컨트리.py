from collections import defaultdict, Counter

t = int(input())

for _ in range(t):
    
    n = int(input())
    team_number = list(map(int, input().split()))
    
    count = Counter(team_number)
    teams = defaultdict(list)
    
    # 완료 선수가 6명이상
    rank = 1
    for team in team_number:
        if count[team] >= 6:
            teams[team].append(rank)
            rank += 1
        
    winner = None
    best_score = float('inf')
    best_fifth = float('inf')
    
    for team, order in teams.items():
        if len(order) < 6:
            continue
        
        # 상위 4명 점수 합
        score = sum(order[:4])
        
        # 5번째 선수 순위
        fifth = order[4]
        
        # 우승 조건
        if score < best_score:
            best_score = score
            best_fifth = fifth
            winner = team
            
        # 동일 점수
        elif score == best_score:
            if fifth < best_fifth:
                best_fifth = fifth
                winner = team
                
    print(winner)