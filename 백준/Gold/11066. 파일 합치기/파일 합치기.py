t = int(input())

for _ in range(t):
    k= int(input())
    x = list(map(int, input().split()))

    # 누적 합
    s = [0] * (k+1)
    for i in range(1, k+1):
        s[i] = s[i-1] + x[i-1]

    # dp[i][j] : i~j 최소 비용
    dp = [[0] * (k+1) for _ in range(k+1)]

    # length : 파일 길이
    for length in range(1, k):
        for i in range(1, k - length + 1):
            j = i + length
            dp[i][j] = int(1e9)

            # 합치는 기준 m
            for m in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j] + s[j] - s[i-1])

    # 1부터 k까지 합치기
    print(dp[1][k])