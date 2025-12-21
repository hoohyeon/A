n = int(input())
A = list(map(int, input().split()))

# dp[i] = i번째를 마지막으로 하는 수열 최대 합
dp = A[:]

for i in range(n):
    for j in range(i):
        # 이번 원소가 이전 원소보다 크면 
        if A[i] > A[j]:
            # max(이전까지의 합, 이번 원소 포함)
            dp[i] = max(dp[i], dp[j] + A[i])
            
print(max(dp))