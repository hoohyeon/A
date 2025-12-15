n = int(input())
weight= {}

for _ in range(n):
    word = input()

    # 1의 자리부터 십진수 가중치
    for pos, ch in enumerate(reversed(word)):
        if not ch in weight:
            weight[ch] = 10 ** pos

        else:
            weight[ch] += 10 ** pos

# 가중치 기준 역순 정렬
sorted_weight = sorted(weight.items(), key=lambda x:x[1], reverse=True)

# 9부터 대입
digit = 9
total = 0

for ch, weight in sorted_weight:
    total += weight * digit
    digit -= 1

print(total)