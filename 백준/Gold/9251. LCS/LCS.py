# LCS(Longest Common Subsequence, 최장 공통 부분 수열)
# != 최장 공통 문자열(Longest Common Substring)

sub1 = input()
sub2 = input()

n1 = len(sub1)
n2 = len(sub2)

# index 0 = margin
dp = [[0] * (n2+1) for _ in range(n1+1)]

for i in range(n1+1):
    for j in range(n2+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
            
        elif sub1[i-1] == sub2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
print(dp[n1][n2])