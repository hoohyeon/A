n = int(input())

drinks = list(map(int, input().split()))

drinks.sort()

max_drink = drinks[n-1]
for i in range(n-1):
    max_drink += drinks[i]/2
    
print(max_drink)