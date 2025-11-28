from collections import Counter

s = input()
n = int(input())
m = len(s)
words = [input() for _ in range(n)]
words_info = [(w, len(w), Counter(w)) for w in words]

# dp[i] = 인덱스 i까지의 최소 비용
inf = 10**9
dp = [inf] * (m + 1)
dp[0] = 0

# 비용 계산
def hamming(a, b):
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1

    return cnt

for i in range(m):
    # 인덱스 i 까지 만들 수 없으면
    if dp[i] == inf:
        continue

    # 후보 단어 테스트
    for w, l, wcnt in words_info:
        j = i + l

        if j > m:
            continue

        seg = s[i:j]

        # 현재 단어(w) 로 붙일 수 있다면  
        if Counter(seg) == wcnt:
            cost = hamming(seg, w)
            dp[j] = min(dp[j], dp[i] + cost)

print(dp[m] if dp[m] != inf else -1)