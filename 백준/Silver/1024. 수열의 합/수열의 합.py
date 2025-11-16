n, l = map(int, input().split())

found = False

for k in range(l, 101):
    
    temp = n - (k * (k-1) // 2)
    
    if temp < 0:
        break
    
    if temp % k == 0:
        
        x = temp // k
        
        for i in range(k):
            
            print(x+i, end=' ')
            
        found = True
        
        break

if not found:
    print(-1)