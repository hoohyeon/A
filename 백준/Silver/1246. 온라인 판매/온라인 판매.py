n, m = map(int, input().split())
price = [int(input()) for _ in range(m)]
price.sort()

max_total, p = 0, 0
for i in range(m):
    total = price[i] * min((m-i), n)

    if total > max_total:
        max_total = total
        p = price[i]
        
print(p, max_total)