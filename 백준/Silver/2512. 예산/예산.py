n = int(input())
budget = list(map(int, input().split()))
max_b = int(input())
left, right = 0, max(budget)

while left <= right:
    m = (left + right) // 2

    total_b = 0
    for b in budget:
        if b >= m:
            total_b += m
        else:
            total_b += b

    if total_b > max_b:
        right = m - 1
    else:
        left = m + 1
    
print(right)