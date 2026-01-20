n = int(input())

# True : SK, False : CY
dp = [True] * (n+1)

if n >= 1:
    dp[1] = True

if n >= 2:
    dp[2] = False

if n >= 3:
    dp[3] = True

if n >= 4:
    dp[4] = True

# 1, 3, 4개를 가져가는 경우 중 하나라도 False (선이 바뀌기 때문에)
if n >= 5:
    for i in range(5, n+1):
        dp[i] = (not dp[i-1]) or (not dp[i-3]) or (not dp[i-4])

if dp[n]:
    print('SK')
else:
    print('CY')