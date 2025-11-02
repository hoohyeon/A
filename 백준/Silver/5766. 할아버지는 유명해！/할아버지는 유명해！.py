while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    rank = {}

    for _ in range(n):
        scores = list(map(int, input().split()))
        
        for score in scores:
            if score not in rank:
                rank[score] = 1
            else:
                rank[score] += 1
          
    sorted_rank = sorted(rank.items(), key= lambda x:(-x[-1], x[0]))
          
    second_score = sorted_rank[1][1]
    
    for i in sorted_rank:
        if i[1] == second_score:
            print(i[0], end=' ')
    
    print()