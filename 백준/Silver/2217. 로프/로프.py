n = int(input())

k = [int(input()) for _ in range(n)]
k.sort()

answers = []
for x in k:
    answers.append(x*n)
    n -= 1

print(max(answers))