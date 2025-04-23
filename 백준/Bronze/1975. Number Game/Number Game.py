t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    
    for b in range(2, n+1):
        temp = n
        
        while temp % b == 0 and temp > 0:
            temp //= b
            ans += 1
    print(ans)