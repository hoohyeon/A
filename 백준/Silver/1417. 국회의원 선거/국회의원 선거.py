n = int(input())
vote = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
    
else:
    dasom = vote[0]
    other = vote[1:]
    cnt = 0

    while True:
        other.sort(reverse=True)

        if dasom <= other[0]:
            dasom += 1
            other[0] -= 1
            cnt += 1
            
        else:
            break
        
    print(cnt)