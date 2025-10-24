cash = int(input())
prices = list(map(int, input().split()))

j_cash, s_cash = cash, cash
j_stock, s_stock = 0, 0

for p in prices:
    while j_cash >= p:
        j_cash -= p
        j_stock += 1
        
j_cash_final = j_stock * prices[-1] + j_cash

for i in range(3, 14):
    if prices[i-3] < prices[i-2] < prices[i-1]: # 3일 연속 상승
        s_cash += prices[i] * s_stock
        s_stock = 0
        
    elif prices[i-3] > prices[i-2] > prices[i-1]: # 3일 연속 하락
        while s_cash >= prices[i]:
            s_cash -= prices[i]
            s_stock += 1
            
s_cash_final = s_stock * prices[-1] + s_cash

if j_cash_final > s_cash_final:
    print('BNP')
elif j_cash_final < s_cash_final:
    print('TIMING')
else:
    print('SAMESAME')