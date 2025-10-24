n = int(input())

cnt = 0

cows = [2] * 11

for _ in range(n):
    number, location = map(int, input().split())
    
    if cows[number] == 2:
        cows[number] = location
        
    elif cows[number] != location:
        cows[number] = location
        
        cnt += 1
    
print(cnt)