while True:
    n, m = input().split()

    n = int(n)
    m = int(round(100 * float(m)))

    if n == 0 and m == 0:
        break

    dp = [0] * (m + 1)
    
    for _ in range(n):
        c, p = input().split()
    
        c = int(c)
        p = int(round(100 * float(p)))
        
        for i in range(p, m + 1):
            dp[i] = max(dp[i], dp[i-p] + c)

    print(max(dp))