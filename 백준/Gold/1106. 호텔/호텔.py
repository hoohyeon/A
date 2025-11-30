c, n = map(int, input().split())
city = [tuple(map(int, input().split())) for _ in range(n)]

max_people = max(p for _, p in city)
m = c + max_people

dp = [int(1e9)] * (m+1)
dp[0] = 0

for cost, people in city:
    for i in range(people, m + 1):
        dp[i] = min(dp[i], dp[i-people] + cost)
            
print(min(dp[c:]))