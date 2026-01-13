n, m = map(int, input().split())
day_page = [tuple(map(int, input().split())) for _ in range(m)]

dp = [0] * (n+1)
for day, page in day_page:
    for i in range(n, day-1, -1):
        dp[i] = max(dp[i], dp[i-day] + page)

print(max(dp))