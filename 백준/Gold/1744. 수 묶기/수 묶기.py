n = int(input())

plus, minus = [], []

result = 0

for _ in range(n):
    num = int(input())

    if num > 1:
        plus.append(num)

    elif num <= 0:
        minus.append(num)

    else:
        result += num
        
plus.sort(reverse=True)
minus.sort()

p, m = len(plus), len(minus)

for i in range(0, p, 2):
    if i+1 == p:
        result += plus[i]
    else:
        result += plus[i] * plus[i+1]

for j in range(0, m, 2):
    if j+1 == m:
        result += minus[j]
    else:
        result += minus[j] * minus[j+1]

print(result)