import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi += sushi

count = [0] * (d + 1)
distinct = 0

# 초기 윈도우 
for i in range(k):
    if count[sushi[i]] == 0:
        distinct += 1

    count[sushi[i]] += 1
  
# 초기 윈도우 결과 (0 초기화 X)
max_distinct = distinct + (1 if count[c] == 0 else 0)

# 슬라이딩
for i in range(1, n):
    left = sushi[i-1]
    count[left] -= 1
    if count[left] == 0:
        distinct -= 1

    right = sushi[i-1 + k]
    count[right] += 1
    if count[right] == 1:
        distinct += 1

    max_distinct = max(max_distinct, distinct + (1 if count[c] == 0 else 0))

print(max_distinct)