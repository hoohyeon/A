n = int(input())
load = list(map(int, input().split()))
price = list(map(int, input().split()))

total, min_price = 0, price[0]

for i in range(n-1):
    if min_price > price[i]:
        min_price = price[i]

    total += load[i] * min_price

print(total)        