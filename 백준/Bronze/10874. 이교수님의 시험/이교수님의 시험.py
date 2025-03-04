n = int(input())
ans = [((i-1) % 5) + 1 for i in range(1, 11)]

for i in range(1, n+1):
    li = list(map(int, input().split()))
    
    if li == ans:
        print(i)