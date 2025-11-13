n, new_score, p = map(int, input().split())

if n == 0:
    print(1)
    
else:
    rank  = list(map(int, input().split()))
    
    if n == p and rank [-1] >= new_score:
        print(-1)

    else:
        result = n + 1

        for i in range(n):
            if rank[i] <= new_score:
                result = i + 1
                break
                
        print(result)