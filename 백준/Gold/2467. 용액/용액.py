n = int(input())
x = list(map(int, input().split()))

# two pointer
left, right = 0, n-1
best_left, best_right = left, right
m = abs(x[left] + x[right])

while left < right:
    sum_val = (x[left] + x[right])
    abs_sum = abs(sum_val)

    # 최솟값 갱신
    if m > abs_sum:
        m = abs_sum
        best_left = left
        best_right = right

    # 합 더 크게
    if sum_val < 0:
        left += 1

    # 합 더 작게
    else:
        right -= 1
    
print(x[best_left], x[best_right])