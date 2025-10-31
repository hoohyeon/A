n = int(input())

dairy_products = [int(input()) for _ in range(n)]

dairy_products.sort(reverse=True)

sales = 0
for i in range(2, n, 3):
    sales += dairy_products[i]

print(sum(dairy_products) - sales)