n = int(input())
customers = list(map(int, input().split()))
computers = [0] * 101

cnt = 0
for c in customers:
    if computers[c] == 0:
        computers[c] = 1
    
    else:
        cnt += 1
        
print(cnt)