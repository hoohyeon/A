n, m = map(int, input().split())

# profit[i][j] : i 기업에 j 원 투자 이익
profit = [[0] * (n+1) for _ in range(m+1)]
for _ in range(n):
    row = list(map(int, input().split()))
    money = row[0]

    for i in range(1, m+1):
        profit[i][money] = row[i]

# dp[i][j] : i기업까지 j원으로 최대 이익
# 정확히 j원을 쓰는 경우이므로 -INF로 초기화
# choice[i][j] : 최대 이익일 때 profit[i][j]
INF = -(1e9)
dp = [[INF] * (n+1) for _ in range(m+1)]
choice = [[0] * (n+1) for _ in range(m+1)]
dp[0][0] = 0

for i in range(1, m+1):
    for j in range(n+1):
        # 이전까지의 최대 이익 가져오기
        dp[i][j] = dp[i-1][j]
        
        for k in range(j+1):
            # i 기업에 k원 투자했을 때 총 이익
            new_profit = dp[i-1][j-k] + profit[i][k]

            # 새로운 이익이 더 클 경우
            if dp[i][j] < new_profit:
                dp[i][j] = new_profit
                choice[i][j] = k

# invest[i] : i 기업에 투자하는 금액
invest = [0] * (m+1)

# 기업 번호, 투자 금액
# 마지막 기업부터 역추적 기록
company, money = m, n
while company > 0:
    invest_money = choice[company][money]

    invest[company] = invest_money
    company -= 1
    money -= invest_money

print(dp[m][n])
print(*invest[1:])