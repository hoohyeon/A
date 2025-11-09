n, start, end = map(int, input().split())

round = 0
while start != end:
    start -= start // 2
    end -= end // 2
    round += 1
    
print(round)