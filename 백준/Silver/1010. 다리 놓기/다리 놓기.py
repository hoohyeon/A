import sys
input = sys.stdin.readline

def dp_factorial(x):
    dp = [0] * (x+1)
    dp[0] = 1
    
    for i in range(1, x+1):
        dp[i] = i * dp[i-1]
        
    return dp[x]

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    
    print(dp_factorial(b) // dp_factorial(a) // dp_factorial(b-a))