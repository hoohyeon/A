n = int(input())
l = list(map(int, input().split()))
j = list(map(int, input().split()))

dp = [0] * 101

for i in range(n):
    loss, joy = l[i], j[i]
    
    for hp in range(99, loss - 1, -1):
        dp[hp] = max(dp[hp], dp[hp - loss] + joy)
        
print(max(dp))