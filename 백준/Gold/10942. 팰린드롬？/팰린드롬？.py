import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
m = int(input())

# dp[i][j] : i번째부터 j번째까지 팰린드롬 = True
dp = [[False] * (n+1) for _ in range(n+1)]

for length in range(1, n+1):
    # 시작 인덱스
    for i in range(1, n - length + 2):

        j = i + length - 1
        
        # 길이가 1 : 팰린드롬
        if length == 1:
            dp[i][j] = True
            
        # 길이가 2 : 두 수가 같을 때
        elif length == 2:
            if x[i-1] == x[j-1]:
                dp[i][j] = True
                
        # 길이가 3 이상 : 양 끝이 같고, 내부가 팰린드롬일 때
        else:
            if x[i-1] == x[j-1] and dp[i+1][j-1]:
                dp[i][j] = True

for _ in range(m):
    s, e = map(int, input().split())

    if dp[s][e]:
        print(1)
    else:
        print(0)