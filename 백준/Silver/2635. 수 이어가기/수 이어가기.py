n = int(input())

best_seq = []
for second in range(n+1):
    s = [n, second]
    
    while True:
        next_num = s[-2] - s[-1]
        
        if next_num < 0:
            break
        
        s.append(next_num)
    
    if len(s) > len(best_seq):
        best_seq = s
        
print(len(best_seq))
print(*best_seq)