import sys
input = sys.stdin.readline

n = int(input())

T, P = [0], [0]
for _ in range(n):
    ti, pi = map(int, input().split())
    T.append(ti)
    P.append(pi)

# 0일, 마지막 날 일한 수익까지 저장하기 위해 n+2
dp = [0] * (n+2)

for day in range(1, n+1):
    # 오늘 상담 안 하는 경우
    dp[day] = max(dp[day], dp[day-1])

    # 오늘 상담 하는 경우
    # 퇴사 전에 상담을 마칠 수 있다면
    if day + T[day] - 1 <= n:
        # 현재 일을 하는 게 이득이라면
        if dp[day + T[day]] < dp[day] + P[day]:
            dp[day + T[day]] = dp[day] + P[day]

print(max(dp))