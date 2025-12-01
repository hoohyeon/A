n = int(input())
m = 1_000_000_000

if n == 0:
    print(0)
    print(0)

else:
    k = abs(n)
    
    a, b = 0, 1
    for _ in range(k):
        a, b = b, (a + b) % m
    
    v = a
    
    if n > 0:
        print(1)
    
    else:
        if n % 2 == 1:
            print(1)
        else:
            print(-1)
    print(v)