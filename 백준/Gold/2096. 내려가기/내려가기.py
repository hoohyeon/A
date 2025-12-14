n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

for _ in range(n):
    score = list(map(int, input().split()))
    
    # 메모리 조건으로 dp 테이블 갱신
    max_dp = [max(max_dp[0], max_dp[1]) + score[0],
              max(max_dp[0], max_dp[1], max_dp[2]) + score[1],
              max(max_dp[1], max_dp[2]) + score[2]]
    
    min_dp = [min(min_dp[0], min_dp[1]) + score[0],
            min(min_dp[0], min_dp[1], min_dp[2]) + score[1],
            min(min_dp[1], min_dp[2]) + score[2]]
    
print(max(max_dp), min(min_dp))