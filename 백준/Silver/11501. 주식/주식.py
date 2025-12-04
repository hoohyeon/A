t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    max_price, profit = 0, 0
    
    for price in reversed(stock):      
        if price < max_price:
            profit += (max_price - price)

        else:
            max_price = price

    print(profit)