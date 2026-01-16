n = int(input())
m = int(input())
ingredient = list(map(int, input().split()))
ingredient.sort()

cnt = 0
left, right = 0, n-1
while left < right:
    s = ingredient[left] + ingredient[right]
    
    if s < m:
        left += 1

    elif s > m:
        right -= 1
        
    elif s == m:
        cnt += 1
        left += 1
        right -= 1

print(cnt)