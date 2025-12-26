t = int(input())

for _ in range(t):
    n = int(input())
    team_num = list(map(int, input().split()))
    
    team_count = {}
    for team in team_num:
        if team in team_count:
            team_count[team] += 1
        else:
            team_count[team] = 1
            
    team_rank = {}
    rank = 1
    for team in team_num:
        if team_count[team] >= 6:
            if team not in team_rank:
                team_rank[team] = []
            team_rank[team].append(rank)
            rank += 1
    
    winner = None
    best_score = float('inf')
    best_fifth = float('inf')
    
    for team, ranks in team_rank.items():
        score = sum(ranks[:4])
        fifth = ranks[4]
        
        if score < best_score:
            best_score = score
            best_fifth = fifth
            winner = team
            
        elif score == best_score:
            if fifth < best_fifth:
                best_fifth = fifth
                winner = team
                
    print(winner)